# Eye & Head Gesture-Based Hands-Free Media Control System 🎥👁️

A real-time **computer vision–based hands-free media control system** that allows users to control YouTube playback using **eye and head gestures**.
The system is implemented using **Python, OpenCV, and MediaPipe Face Mesh**.

---

## ✨ Features

* 👁️ Double Blink → Play / Pause
* 😴 Long Blink → Mute / Unmute
* 👀 Look Left → Rewind video
* 👀 Look Right → Forward video
* 🧠 Head Turn (Yaw) → Fast skip
* 🔊 Head Tilt → Volume control
* 🤖 Smart Auto-Pause when face disappears or sudden distraction occurs

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe Face Mesh
* NumPy
* Pynput

---

## 🧩 System Workflow

1. Capture webcam video
2. Detect facial landmarks using MediaPipe
3. Compute Eye Aspect Ratio (EAR)
4. Detect eye blink and gaze direction
5. Estimate head yaw and tilt
6. Map gestures to media control actions
7. Trigger keyboard events in real time

---

## 💻 How to Run

```bash
pip install -r requirements.txt
python src/eye_head_gesture_control.py
```

⚠️ Keep the YouTube tab focused for keyboard controls to work.

---

## 🎯 Applications

* Assistive technology
* Touchless human–computer interaction
* Smart media systems
* Computer vision research

---

## 🔮 Future Scope

* Gesture customization
* Multi-platform media support
* Embedded system deployment
* AI-based gesture classification

---

## 👤 Author

**Rithwika PG**
Robotics & Automation Engineering Student
Sahyadri College of Engineering and Management
