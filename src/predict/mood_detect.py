import cv2
import numpy as np
from keras.models import load_model

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier('predict/haarcascade_frontalface_default.xml')

# Load the pre-trained emotion recognition model
emotion_model = load_model('predict/fer2013_mini_XCEPTION.102-0.66.hdf5', compile=False)

# Define emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Function to detect emotions from an image object
def detect_emotions(image):
    try:
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        emotions = []

        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]

            # Resize the face ROI for emotion recognition
            face_roi = cv2.resize(face_roi, (64, 64))
            face_roi = face_roi.astype('float32') / 255.0
            face_roi = face_roi - 0.5
            face_roi = face_roi * 2.0

            # Prepare the input blob for the emotion recognition model
            blob = cv2.dnn.blobFromImage(face_roi, 1.0, (64, 64), (0, 0, 0), swapRB=True, crop=False)
            
            # Make sure the blob has the correct depth (32-bit float)
            blob = blob.astype('float32')

            # Transpose the blob to match the model's input shape
            blob = np.transpose(blob, (0, 2, 3, 1))

            # Set the input blob for the model and perform forward pass
            emotion_prediction = emotion_model.predict(blob)

            # Get the emotion label with the highest confidence
            emotion_label = emotion_labels[np.argmax(emotion_prediction)]
            emotions.append(emotion_label)

        return emotions

    except Exception as e:
        print(f"Error in detect_emotions: {str(e)}")
        return []

# Load your image using cv2.imread() here
# image = cv2.imread('path_to_your_image.jpg')

# Example usage:
# moods = detect_emotions(image)
# print("Detected emotions:", moods)
