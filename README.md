# Python-Hand-Face-Detector
The following Python code uses the MediaPipe library to detect both hands and faces.

This code captures video from the default camera (specified by the 0 argument to cv2.VideoCapture()) and processes each frame with the MediaPipe hand detection and face detection modules. The resulting hand landmark map and face bounding boxes are drawn on the image using the drawing utilities of MediaPipe. The resulting image is displayed in a window named "Hand and Face Detection". The program exits when the Esc key is pressed.

Note that the program assumes that you have installed the MediaPipe library and its dependencies. You can install it using pip: pip install mediapipe.

Just 'python detector.py' and you are good to go
