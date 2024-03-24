Hand Gesture Volume Control

Introduction:
This project utilizes computer vision techniques to detect hand landmarks and adjust the system volume accordingly.

Files:
1. hand_gesture.py: Python script for capturing webcam input, processing hand gestures, and adjusting system volume based on detected gestures.
   
2. handModule.py: Module containing the handDetector class, which utilizes the MediaPipe library to detect and track hand landmarks in the webcam feed.

Usage:
1. Ensure Python and necessary libraries (OpenCV, MediaPipe, comtypes) are installed.
2. Run hand_gesture.py.
3. A window will open displaying the webcam feed with hand landmarks drawn.
4. Perform hand gestures within the webcam frame to control volume.

Hand Gestures:
- Volume Increase: Bring thumb and index finger closer.
- Volume Decrease: Spread thumb and index finger apart.
- Mute: Bring thumb and index finger together with a small distance between them.
