# Blink to Communicate – Helping LIS People

## 📌 Problem Statement

People with Locked-in Syndrome (LIS) face difficulty in communicating their basic needs.
This project enables communication using eye blinks detected through a laptop webcam.

## 🎯 Objective

To detect eye blinks using computer vision and convert them into meaningful messages.

## 🧠 Technology Used

- Python
- OpenCV
- MediaPipe
- cvzone
- Webcam

## ⚙️ How It Works

- Camera captures the user's face
- Eye landmarks are detected
- Blink count is calculated
- Each blink pattern maps to a message

| Blink Count | Message                      |
| ----------- | ---------------------------- |
| 1 Blink     | I need water                 |
| 2 Blinks    | I need food                  |
| 3 Blinks    | I want to go to the washroom |

## ▶️ How to Run

```bash
pip install opencv-python mediapipe cvzone
python blink_detection.py
```
