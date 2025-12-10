import cv2
import numpy as np
import os

# Load standard face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def analyze_image(image_stream):
    # 1. Read Image
    file_bytes = np.frombuffer(image_stream.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    image_stream.seek(0) # Reset file pointer

    if image is None: return False, 0, "Image error"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Check Blur
    score = cv2.Laplacian(gray, cv2.CV_64F).var()
    if score < 100:
        return False, score, "Image too blurry. Hold steady."

    # 3. Check for Face
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        return False, score, "No face detected. Please align ID photo."

    return True, score, "Image Accepted"