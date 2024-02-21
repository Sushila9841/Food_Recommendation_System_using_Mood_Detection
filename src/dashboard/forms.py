# import Form class from django.forms
from django import forms
from food.models import Food, FoodCategory

# Create a form class
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = "__all__"

