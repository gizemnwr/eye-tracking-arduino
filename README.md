# 👁️ Eye Tracking Communication System with Arduino Integration

This is a simple and powerful **eye-tracking-based communication system** designed to help individuals with limited mobility or speech capabilities. By tracking eye gaze directions, it triggers predefined messages and sends commands to an Arduino to potentially control external devices.

---

## 🚀 Features

- 🔍 Real-time eye gaze detection using OpenCV and Dlib
- 💬 Sends visual messages via GUI (Tkinter)
- 🧠 Recognizes 3 directions: **Left**, **Center**, and **Right**
- 📟 Sends corresponding signals to Arduino for further action (e.g., LEDs, buzzers, etc.)

---

## 🎯 Use Case

This system is particularly designed for:
- Individuals with ALS, paralysis, or speech impairments
- Communication in emergency or care environments

---

## 🧰 Technologies Used

- Python 3
- OpenCV
- Dlib (68 face landmarks)
- Tkinter (GUI)
- Arduino (Serial communication via pySerial)

---

## 🔧 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gizemnwr/eye-tracking-arduino.git
cd eye-tracking-arduino

2. Install Dependencies
pip install opencv-python dlib numpy pyserial
💡 You also need to download the file shape_predictor_68_face_landmarks.dat
Download link (official):
Unzip and place it on your Desktop.

🖥️ Running the Program
Simply run the Python file:
python goz_takip.py

Make sure your Arduino is connected via USB, and the correct COM port is defined in the code.

📡 Arduino Connection
Left eye gaze ➡️ sends 'L' → "I need water"

Right eye gaze ➡️ sends 'R' → "I'm hungry"

Center ➡️ sends 'C' → "I need help"

Use this data on Arduino to control devices accordingly.

🧠 How It Works
Face is detected using Dlib's 68-landmark model.

Left eye region is isolated.

The white area of the eye is processed to determine the pupil’s position.

Direction is mapped to a message and sent via serial port.


👩‍💻 Author
gizemnwr


📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and share! 🚀
