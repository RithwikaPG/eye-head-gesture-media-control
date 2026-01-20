#!/usr/bin/env python3
import cv2
import time
import math
import numpy as np
import mediapipe as mp
from collections import deque
from pynput.keyboard import Controller, Key

keyboard = Controller()

EAR_THRESHOLD = 0.25
DOUBLE_BLINK_GAP = 0.4
LONG_BLINK_TIME = 1.0
GAZE_THRESHOLD = 0.35
COOLDOWN = 0.8

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

cap = cv2.VideoCapture(0)
mp_face = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

blink_time = 0
eye_closed = False
gaze_history = deque(maxlen=5)
last_action = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = mp_face.process(rgb)

    if res.multi_face_landmarks:
        lm = res.multi_face_landmarks[0].landmark

        left_eye = [np.array([lm[i].x * w, lm[i].y * h]) for i in LEFT_EYE]
        right_eye = [np.array([lm[i].x * w, lm[i].y * h]) for i in RIGHT_EYE]

        ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2

        if ear < EAR_THRESHOLD and not eye_closed:
            eye_closed = True
            blink_time = time.time()

        elif ear >= EAR_THRESHOLD and eye_closed:
            duration = time.time() - blink_time
            eye_closed = False

            if duration > LONG_BLINK_TIME:
                keyboard.press('m'); keyboard.release('m')
            elif time.time() - last_action < DOUBLE_BLINK_GAP:
                keyboard.press('k'); keyboard.release('k')

            last_action = time.time()

    cv2.imshow("Eye & Head Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
