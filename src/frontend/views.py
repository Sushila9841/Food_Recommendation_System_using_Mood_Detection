from django.shortcuts import render
from django.views.generic import View
from predict.forms import CameraForm
from django.http import HttpResponse
from predict.mood_detect import detect_emotions
from predict.food_detect import detect_food
from random import randint
import numpy as np
import cv2
from blogs.models import Blog
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from userprofile.mixin import LoginRequired
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from predict.moods import Moods
from food.models import Food
from userprofile.models import MoodHistory
from frontend.forms import FoodVsMoodForm , feedbackForm
from .models import feedback
from django.contrib import messages


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'frontend/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        usr = authenticate(username=username, password=password)
        if usr is not None:
            if usr.username == 'admin':
                login(self.request, usr)
                return redirect('/dashboard')
            login(self.request, usr)
            user_profile = UserProfile.objects.get(user=usr)
            if user_profile.has_filled_survey:
                return redirect('/camera')
            else:
                return redirect('/questions')
        else:
            context = {
                "error": "incorrect credentials"
            }
            return render(request, 'frontend/login.html', context)
        
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
        
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/signup.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        age = int(request.POST["age"])
        phone = request.POST["phone"]
        address = request.POST["address"]
        gender = request.POST["gender"]
        if User.objects.filter(username=username).exists():
            context={
                "error":"Username already taken"
            }
            return render(request, 'frontend/signup.html', context)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        userprofile = UserProfile.objects.create(user=user, age=age, phone_number=phone, address=address, gender=gender)
        userprofile.save()  
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/questions')
        return render(request, 'frontend/signup.html')

    

class HomePage(View):

    def get(self, request, *args, **kwargs):
        star_positions = [{'top': randint(0, 100), 'left': randint(0, 100)} for _ in range(30)]
        context = {
            'star_positions': star_positions,
            # ... you can add any other context variables here if needed
        }
         
        return render(request, 'frontend/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'frontend/about.html')
    
class Contact(View):
    def get (self, request, *args, **kwargs):
        form = feedbackForm()
        return render(request, "frontend/contact.html", {'form': form})
    

    def post(self, request, *args, **kwargs):
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Sucessfully received your Feedback")
            return redirect("contact")
        else:
             return render(request, 'frontend/contact.html', {'form': form})

class Footer(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'frontend/footer.html')
    
class BlogsView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }

        return render(request, 'frontend/blogs.html', context)
    
class BlogView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        blog = Blog.objects.get(pk=pk)
        context = {
            'blog': blog
        }   
        return render(request, 'frontend/blog_single.html', context)
    

class Camera(LoginRequired, View):
    def get(self, request, *args, **kwargs):
    
        return render(request, 'frontend/camera.html')
    
    def post(self, request, *args, **kwargs):
        # get image file image object from request.FILES
        captured_image_data = request.FILES.get('image_file')
        if captured_image_data:
            # Read the image data from the uploaded file
            image_bytes = captured_image_data.read()

            # Convert the image data to a NumPy array
            nparr = np.frombuffer(image_bytes, np.uint8)

            # Decode the NumPy array to an OpenCV image
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Perform emotion detection on the image
            moods = detect_emotions(image)
            mood = moods[0]
            foods = detect_food('happy', 11, 'm')
        if 'Happy' in moods:
            foods = Food.objects.filter(food_category=Moods.happy)
        elif 'Sad' in moods:
            foods = Food.objects.filter(food_category=Moods.sad)
        elif 'Angry' in moods:
            foods = Food.objects.filter(food_category=Moods.angry)
        elif 'Surprised' in moods:
            foods = Food.objects.filter(food_category=Moods.surprised)
        elif 'Fearful' in moods:
            foods = Food.objects.filter(food_category=Moods.fearful)
        elif 'Disgusted' in moods:
            foods = Food.objects.filter(food_category=Moods.disgusted)
        else:
            foods = Food.objects.filter(food_category=Moods.neutral)

        mood_history = MoodHistory.objects.create(user=request.user, mood=moods[0])
        mood_history.save()
        context = {
            'foods': foods,
            'moods': moods
        }

        return render(request, 'frontend/food_suggest.html', context)
    
class QuestionsView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        form = FoodVsMoodForm()
        context = {
            'form': form
        }
        return render(request, 'frontend/questions.html', context)
    
    def post(self, request, *args, **kwargs):
        form = FoodVsMoodForm(request.POST)
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.has_filled_survey = True
        user_profile.save()
        return redirect('/camera')
   