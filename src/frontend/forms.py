from django import forms
from food.models import FoodCategory
from .models import feedback

# add food category in choices 
food_cat = FoodCategory.objects.all()
# add this food FoodCategory to choices 
CHOICES = []
for cat in food_cat:
    CHOICES.append((cat.id, cat.name))
    

class FoodVsMoodForm(forms.Form):
    #char fields with choices
    q1 = forms.CharField(label='When you are feeling happy, what type of food do you crave the most?', widget=forms.RadioSelect(choices=CHOICES))
    q2 = forms.CharField(label='When you are feeling sad, what type of food do you crave the most?', widget=forms.RadioSelect(choices=CHOICES))
    q3 = forms.CharField(label='When you are feeling angry, what type of food do you crave the most?', widget=forms.RadioSelect(choices=CHOICES))
    q4 = forms.CharField(label='When you are feeling neutral, what type of food do you crave the most?', widget=forms.RadioSelect(choices=CHOICES))
    q5 = forms.CharField(label='When you are feeling surprised, what type of food do you crave the most?', widget=forms.RadioSelect(choices=CHOICES))
    q6 = forms.CharField(label='When you are feeling fearful, what type of food do you crave the most?', widget=forms.RadioSelect(choices=CHOICES))
    q7 = forms.CharField(label='When you are feeling disgusted, what type of food do you crave the most?', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']
        labels = {
            'q1': 'When you are feeling happy, what type of food do you crave the most?',
            'q2': 'When you are feeling sad, what type of food do you crave the most?',
            'q3': 'When you are feeling angry, what type of food do you crave the most?',
            'q4': 'When you are feeling neutral, what type of food do you crave the most?',
            'q5': 'When you are feeling surprised, what type of food do you crave the most?',
            'q6': 'When you are feeling fearful, what type of food do you crave the most?',
            'q7': 'When you are feeling disgusted, what type of food do you crave the most?',
        }
        widgets = {
            'q1': forms.RadioSelect(choices=CHOICES),
            'q2': forms.RadioSelect(choices=CHOICES),
            'q3': forms.RadioSelect(choices=CHOICES),
            'q4': forms.RadioSelect(choices=CHOICES),
            'q5': forms.RadioSelect(choices=CHOICES),
            'q6': forms.RadioSelect(choices=CHOICES),
            'q7': forms.RadioSelect(choices=CHOICES),
        }
    
class feedbackForm(forms.ModelForm):
        class Meta:
            model= feedback
            fields=['email', 'message']
            