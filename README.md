# 🧠 Real-Time Face Detection with OpenCV

This project is a simple real-time face detection system using Python and OpenCV.

It captures video from your webcam, detects faces using Haar Cascade classifiers, draws bounding boxes around them, and saves each detected face **only once** to a folder.

---

## 📷 Features

- Real-time face detection from webcam
- Face detection using Haar Cascades
- Green rectangle drawn around each face
- Each detected face is saved only once
- Saved images are stored in a folder called `saved_faces`

---

## 🚀 How to Run

### 1. Clone the repository:

```bash
git clone https://github.com/Utkuersy/Python_Face_Detection_Project.git
cd Python_Face_Detection_Project
```

### 2. Install requirements:

```bash
pip install opencv-python
```

### 3. Run the script:

```bash
python face_detection.py
```

> ✅ Press `q` to quit the webcam window.

---

## 📁 Project Structure

```
Python_Face_Detection_Project/
│
├── face_detection.py       # Main script for face detection
├── saved_faces/            # Folder to store detected face images
└── README.md               # This documentation
```

---

## 🛠 Requirements

- Python 3.7 or higher
- OpenCV (`opencv-python`)

---

## 💡 Future Plans

- Add face recognition support (DeepFace or InsightFace)
- Add logging with timestamps
- Optimize duplicate face detection
- Build a web or mobile interface

---

## 👤 Author

**Utku İlker ERSOY**  
[LinkedIn](https://www.linkedin.com/in/utku-ilker-ersoy-64255620b/)  
[GitHub](https://github.com/Utkuersy)

---
