import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import time

# Initialize the MediaPipe Hands solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize the MediaPipe drawing utilities
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture from the default camera
cap = cv2.VideoCapture(0)

# Variables to track the previous position of the index finger
previous_y = None
last_scroll_time = 0
scroll_cooldown_time = 3  # 3 seconds cooldown

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display, and convert the BGR image to RGB.
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the hand annotations on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the y-coordinate of the index finger tip (landmark 8)
            index_finger_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0]

            if previous_y is not None:
                # Determine the vertical movement
                movement_y = index_finger_tip_y - previous_y

                # Check if enough time has passed since the last scroll
                current_time = time.time()
                if current_time - last_scroll_time >= scroll_cooldown_time:
                    # Scroll up or down based on the movement direction
                    if movement_y < -10:  # Move up
                        pyautogui.scroll(20)
                        last_scroll_time = current_time
                    elif movement_y > 10:  # Move down
                        pyautogui.scroll(-20)
                        last_scroll_time = current_time

            # Update the previous y-coordinate
            previous_y = index_finger_tip_y

    # Show the current frame
    cv2.imshow('Hand Tracking', frame)

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
