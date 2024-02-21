import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the food model
food_model = load_model('predict/food_category_prediction_model.h5')

# Define a function to detect food
def detect_food(mood, age, gender):
    # Example input data for prediction
    input_data = pd.DataFrame({
        "Mood_Angry": [0],
        "Mood_Disgust": [0],
        "Mood_Fear": [0],
        "Mood_Happy": [0],
        "Mood_Sad": [0],
        "Mood_Surprise": [0],
        "Mood_Neutral": [0],
        "Gender_Female": [0],
        "Gender_Male": [0]
    })

    # Set the appropriate mood column to 1 based on the input mood
    if mood == 'Happy':
        input_data['Mood_Happy'] = 1
    elif mood == 'Sad':
        input_data['Mood_Sad'] = 1
    elif mood == 'Angry':
        input_data['Mood_Angry'] = 1
    elif mood == 'Surprise':
        input_data['Mood_Surprise'] = 1
    elif mood == 'Fear':
        input_data['Mood_Fear'] = 1
    elif mood == 'Disgust':
        input_data['Mood_Disgust'] = 1
    else:
        input_data['Mood_Neutral'] = 1
    
    # Set the gender column based on the input gender
    if gender == 'm':
        input_data['Gender_Male'] = 1
    elif gender == 'f':
        input_data['Gender_Female'] = 1

    # Convert input_data to a NumPy array
    input_data = input_data.values

    # Make a prediction using the loaded model
    predicted_food_category = food_model.predict(input_data)
    
    # Find the index of the maximum value to get the predicted class
    predicted_class = np.argmax(predicted_food_category)
    
    return predicted_class

