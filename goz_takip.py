# Eye Tracking Communication System with Arduino Integration
# Author: gizemnwr
# Description: Detects eye gaze direction using OpenCV and dlib to communicate predefined messages
#              via GUI and sends corresponding commands to an Arduino device.

import cv2
import dlib
import numpy as np
import os
import serial
import time
import tkinter as tk
from tkinter import Label

# Attempt to establish connection with Arduino
try:
    arduino = serial.Serial('COM3', 9600)  # Replace with your actual COM port if needed
    time.sleep(2)  # Wait for Arduino to initialize
    print("Successfully connected to Arduino.")
except Exception as e:
    print("Failed to connect to Arduino:", e)
    arduino = None

# Load the facial landmarks predictor model
predictor_path = os.path.join(os.path.expanduser("~"), "Desktop", "shape_predictor_68_face_landmarks.dat")

if not os.path.isfile(predictor_path):
    print("Model file not found:", predictor_path)
    exit()
else:
    print("Model loaded successfully:", predictor_path)

# Initialize face detector and shape predictor
detector = dlib.get_frontal_face_detector()
try:
    predictor = dlib.shape_predictor(predictor_path)
    print("Shape predictor loaded successfully.")
except RuntimeError:
    print("Failed to load shape predictor.")
    exit()

# Start webcam
cap = cv2.VideoCapture(0)

# Create Tkinter GUI window
root = tk.Tk()
root.title("Eye Gaze Communication")
root.geometry("400x300")

message_label = Label(root, text="Messages will appear here", font=("Helvetica", 16), height=6, width=40)
message_label.pack()

def update_message(new_message):
    message_label.config(text=new_message)
    message_label.update()

last_message = None  # Track last sent message to avoid repeats

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye_region = np.array([
            (landmarks.part(36).x, landmarks.part(36).y),
            (landmarks.part(37).x, landmarks.part(37).y),
            (landmarks.part(38).x, landmarks.part(38).y),
            (landmarks.part(39).x, landmarks.part(39).y),
            (landmarks.part(40).x, landmarks.part(40).y),
            (landmarks.part(41).x, landmarks.part(41).y)
        ], dtype=np.int32)

        mask = np.zeros_like(gray)
        cv2.polylines(mask, [left_eye_region], True, 255, 2)
        cv2.fillPoly(mask, [left_eye_region], 255)
        eye = cv2.bitwise_and(frame, frame, mask=mask)

        min_x = np.min(left_eye_region[:, 0])
        max_x = np.max(left_eye_region[:, 0])
        min_y = np.min(left_eye_region[:, 1])
        max_y = np.max(left_eye_region[:, 1])

        eye_frame = frame[min_y:max_y, min_x:max_x]

        gray_eye = cv2.cvtColor(eye_frame, cv2.COLOR_BGR2GRAY)
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(threshold_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            direction = "Center"
        else:
            max_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(max_contour)
            if M['m00'] == 0:
                direction = "Center"
            else:
                cx = int(M['m10'] / M['m00'])
                width = eye_frame.shape[1]
                if cx < width / 3:
                    direction = "Left"
                elif cx > 2 * width / 3:
                    direction = "Right"
                else:
                    direction = "Center"

        # Display message and send command to Arduino based on eye direction
        if direction == "Right" and last_message != "I'm hungry":
            update_message("I'm hungry")
            if arduino:
                arduino.write(b'R')
            last_message = "I'm hungry"
        elif direction == "Left" and last_message != "I need water":
            update_message("I need water")
            if arduino:
                arduino.write(b'L')
            last_message = "I need water"
        elif direction == "Center" and last_message != "I need help":
            update_message("I need help")
            if arduino:
                arduino.write(b'C')
            last_message = "I need help"

    cv2.imshow("Eye Tracking System", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

    root.update_idletasks()
    root.update()

cap.release()
cv2.destroyAllWindows()
root.destroy()

if arduino:
    arduino.close()

