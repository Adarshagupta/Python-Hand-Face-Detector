import cv2
import mediapipe as mp

# Initialize the hand detection module of MediaPipe
mp_hands = mp.solutions.hands

# Initialize the face detection module of MediaPipe
mp_face_detection = mp.solutions.face_detection

# Initialize the drawing utilities of MediaPipe
mp_draw = mp.solutions.drawing_utils

# Initialize the video capture device
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands, \
     mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        # Read a frame from the video capture device
        success, image = cap.read()
        if not success:
            print("Failed to read video")
            break

        # Convert the image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image with MediaPipe to detect hands and faces
        hands_results = hands.process(image)
        face_results = face_detection.process(image)

        # Draw a landmark map of the hands' position
        if hands_results.multi_hand_landmarks:
            for hand_landmarks in hands_results.multi_hand_landmarks:
                mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Draw bounding boxes around the faces
        if face_results.detections:
            for detection in face_results.detections:
                mp_draw.draw_detection(image, detection)

        # Display the resulting image
        cv2.imshow('Hand and Face Detection', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release the video capture device
cap.release()
