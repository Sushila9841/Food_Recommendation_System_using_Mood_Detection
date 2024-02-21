from django.shortcuts import render
from .models import FoodRecommendation
from .your_script_path import detect_emotions, detect_food

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot('FoodRecommendationBot')

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')  # Train on English language data

custom_food_trainer = ListTrainer(bot)
custom_food_data = [
    "I'm sad.",
    "I'm sorry to hear that. How about some comfort food like chocolate or ice cream?",
    
    "I'm happy.",
    "That's great! How about a fresh fruit salad to keep the mood?",
    
    "I'm feeling down.",
    "Perhaps a warm cup of hot chocolate or tea might lift your spirits?",
    
    "I'm elated!",
    "Fantastic! Maybe some sparkling water or a light snack would be perfect?",
    
    "I'm bored.",
    "Sometimes, trying out a new recipe or a snack you haven't had in a while can be exciting.",
    
    "I'm anxious.",
    "Drinking some calming chamomile tea could help. And maybe stay away from caffeine for a bit?",
    
    "I'm angry.",
    "Take a deep breath. Maybe munch on some crunchy snacks like nuts or pretzels to let out some steam.",
    
    "I'm feeling meh.",
    "A smoothie with your favorite fruits might bring a small change. Want to try?",
    
    "I'm excited.",
    "Keep the energy going with some energizing snacks like trail mix or granola bars.",
    
    "I'm sleepy.",
    "A cup of warm milk or caffeine-free herbal tea can be soothing before sleep.",
    
    "I'm energetic.",
    "That's great to hear! Keep hydrated with some fresh water or juice.",
    
    "I feel romantic.",
    "How about sharing a plate of pasta or a nice dessert with someone special?",
    
    "I'm feeling lazy.",
    "Quick and easy snacks like fruits or pre-packaged health bars can be a go-to.",
    
    "I'm feeling motivated.",
    "Keep it up! A balanced meal with proteins and greens would be a great choice.",
    
    "I'm stressed.",
    "Consider foods rich in magnesium or Omega-3, like spinach or fish, which are believed to reduce stress.",
    
    "I feel indifferent.",
    "Sometimes, a classic sandwich or a staple dish can be the way to go.",
    
    "I'm nostalgic.",
    "How about revisiting some of your childhood favorite snacks or dishes?",
    
    "I'm adventurous.",
    "Consider trying out a cuisine or dish you've never had before.",
    
    "I feel unwell.",
    "Make sure to consult with a doctor if it's serious. Light soups or broths can be gentle on the stomach.",
    
    "I feel rejuvenated.",
    "A detox water or salad might complement that feeling.",
    
    "I feel like celebrating.",
    "Pop a bottle of champagne or your favorite drink, and maybe pair it with a nice meal.",
    
    "I feel grateful.",
    "Sharing a meal with loved ones can be a great way to express gratitude.",
    
    "I'm feeling creative.",
    "Experiment in the kitchen. Maybe come up with a new recipe or twist on a classic dish.",
    
    "I'm feeling confident.",
    "Go for a bold dish or something spicy if you like.",
    
    "I feel overwhelmed.",
    "Take a break and have a soothing drink like herbal tea or even just water with a slice of lemon.",
    
    "I'm in the mood for something sweet.",
    "How about a dessert? Maybe some pastries, cakes, or cookies?",
    
    "I want something savory.",
    "Consider dishes like grilled cheese, savory pies, or even a nice steak."
]

custom_food_trainer.train(custom_food_data)
def chat_view(request):
    message = ""
    if request.method == "POST":
        image = request.FILES.get('image') # assuming you're using an image input field with name 'image'
        mood = detect_emotions(image.read())
        
        if mood:
            detected_mood = mood[0] # taking the first detected emotion
            recommended_food = detect_food(detected_mood, age=request.POST.get('age'), gender=request.POST.get('gender'))
            food = FoodRecommendation.objects.filter(mood=detected_mood).first()

            if food:
                message = f"Feeling {detected_mood}? We recommend {food.food}."
            else:
                message = f"Feeling {detected_mood}? Sorry, we don't have a food recommendation for that mood."

    return render(request, 'chatbot.html', {'message': message})
