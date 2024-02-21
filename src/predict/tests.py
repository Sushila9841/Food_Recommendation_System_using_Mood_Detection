from django.test import TestCase

# Create your tests here.
import cv2
import numpy as np
import unittest
from unittest.mock import MagicMock

# Import detect_emotions function here

class TestDetectEmotions(unittest.TestCase):

    def setUp(self):
        self.mock_cascade = MagicMock()
        self.mock_model = MagicMock()
        self.mock_image = np.zeros((100, 100, 3), dtype=np.uint8)

    def test_detect_emotions_with_faces(self):
        self.mock_cascade.detectMultiScale.return_value = [(10, 10, 20, 20)]  # Mock a detected face
        self.mock_model.predict.return_value = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
        
        emotions = detect_emotions(self.mock_image, self.mock_cascade, self.mock_model)
        
        self.assertEqual(emotions, ['Surprise'])  # Assert the expected emotion

    def test_detect_emotions_without_faces(self):
        self.mock_cascade.detectMultiScale.return_value = []  # Mock no detected faces
        
        emotions = detect_emotions(self.mock_image, self.mock_cascade, self.mock_model)
        
        self.assertEqual(emotions, [])  # Assert that no emotions were detected

if __name__ == '__main__':
    unittest.main()