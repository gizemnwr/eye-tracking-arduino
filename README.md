# 👁️ Göz Takibi ile İletişim Sistemi (Arduino Entegrasyonlu)

Bu proje, fiziksel hareket kabiliyeti kısıtlı veya konuşma engeli olan bireylerin iletişim kurabilmesini kolaylaştırmak amacıyla geliştirilen bir **göz takibi tabanlı iletişim sistemidir**.  
Göz yönü algılanarak önceden tanımlanmış mesajlar görüntülenir ve Arduino’ya komut gönderilerek harici cihazlar kontrol edilebilir.

---

## 🚀 Özellikler

- 🔍 Gerçek zamanlı göz yönü tespiti (OpenCV & Dlib kullanılarak)
- 💬 Tkinter ile görsel kullanıcı arayüzü
- 🧠 3 yön algılama: Sol, Orta ve Sağ
- 📟 Arduino'ya seri bağlantı üzerinden sinyal gönderimi

---

## 🎯 Hedef Kullanıcılar

Bu sistem özellikle aşağıdaki durumlar için tasarlanmıştır:

- ALS hastaları, felç geçirmiş bireyler veya konuşma engeli bulunan kişiler  
- Hastane, bakım evi gibi acil müdahale gerektiren ortamlarda iletişim kolaylaştırma

---

## 🧰 Kullanılan Teknolojiler

- Python 3  
- OpenCV  
- Dlib (68 yüz işaret noktası modeli)  
- Tkinter (grafik arayüz için)  
- Arduino (pySerial ile bağlantı sağlanır)

---

## 🔧 Kurulum ve Çalıştırma

### 1. Depoyu Bilgisayarına Klonla

```bash
git clone https://github.com/gizemnwr/eye-tracking-arduino.git
cd eye-tracking-arduino
```

### 2. Gerekli Kütüphaneleri Yükle

```bash
pip install opencv-python dlib numpy pyserial
```

> 💡 Ek olarak `shape_predictor_68_face_landmarks.dat` adlı yüz model dosyasını indirmen gerekiyor.  
İndirme bağlantısı (resmi): [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)  
Dosyayı masaüstüne çıkarıp kodda belirtilen yere yerleştirmeyi unutma.

---

## 🖥️ Programı Başlat

Aşağıdaki komutu kullanarak programı çalıştırabilirsin:

```bash
python goz_takip.py
```

> 📌 Arduino’nun USB ile bağlı olduğundan ve kod içinde doğru COM portunun ayarlandığından emin ol.

---

## 📡 Arduino Bağlantısı

| Göz Yönü   | Gönderilen Mesaj     | Arduino’ya Gönderilen Karakter |
|------------|-----------------------|-------------------------------|
| Sol        | I need water (Su istiyorum) | `L`                         |
| Sağ        | I'm hungry (Açım)         | `R`                         |
| Orta       | I need help (Yardıma ihtiyacım var) | `C`               |

> Arduino tarafında bu karakterleri alıp, LED, buzzer veya farklı çıkış birimleriyle cevap verebilirsin.

---

## 🧠 Sistem Nasıl Çalışır?

1. Dlib ile yüz algılama yapılır (68 nokta).
2. Sol göz bölgesi tespit edilerek izole edilir.
3. Göz bebeğinin beyaz alandaki konumu analiz edilir.
4. Yön bilgisi çıkarılır → GUI’ye mesaj gönderilir → Arduino’ya karakter gönderilir.

---

## 👩‍💻 Geliştirici

**[@gizemnwr](https://github.com/gizemnwr)**

Bu proje, bireysel olarak tarafımdan geliştirilmiştir. ✨

---

## 📜 Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) ile lisanslanmıştır.  
Dilediğiniz gibi kullanabilir, geliştirebilir ve paylaşabilirsiniz. 🎉

---
