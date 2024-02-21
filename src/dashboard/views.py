from django.shortcuts import render
from django.views.generic import View
from userprofile.mixin import LoginRequired
from django.contrib.auth import authenticate, login, logout                 
from userprofile.models import UserProfile as User
from food.models import Food, FoodCategory
from .forms import FoodForm, FoodCategoryForm
from django.shortcuts import redirect
from frontend.models import feedback



class DashBoardView(LoginRequired, View):
    def get(self, request, *args, **kwargs):

        context = {
     

        }
        return render(request, 'dashboard/dashboard.html', context)
    
class FoodListView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        foods = Food.objects.all()
        context = {
            "foods": foods
        }
        return render(request, 'dashboard/food_list.html', context)

class FoodAddView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        form = FoodForm()
        context = {
            "form": form
        }
        return render(request, 'dashboard/food_add.html', context)
    
    def post(self, request, *args, **kwargs):
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
        else:
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, 'dashboard/food_add.html', context)
 

class FoodEditView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        food_id = kwargs["food_id"]
        food = Food.objects.get(id=food_id)
        form = FoodForm(instance=food)
        context = {
            "form": form
        }
        return render(request, 'dashboard/food_add.html', context)
    
    def post(self, request, *args, **kwargs):
        food_id = kwargs["food_id"]
        food = Food.objects.get(id=food_id)
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
        else:
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, 'dashboard/food_add.html', context)
        
class FoodDeleteView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        food_id = kwargs["food_id"]
        food = Food.objects.get(id=food_id)
        food.delete()
        return redirect('food_list')
    
class FoodCategoryListView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        food_categories = FoodCategory.objects.all()
        context = {
            "food_categories": food_categories
        }
        return render(request, 'dashboard/food_cat_list.html', context)

class FoodCategoryAddView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        form = FoodCategoryForm()
        context = {
            "form": form
        }
        return render(request, 'dashboard/food_cat_add.html', context)
    
    def post(self, request, *args, **kwargs):
        form = FoodCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_category_list')
        else:
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, 'dashboard/food_cat_add.html', context)
        
class FoodCategoryEditView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        food_cat_id = kwargs["food_cat_id"]
        food_cat = FoodCategory.objects.get(id=food_cat_id)
        form = FoodCategoryForm(instance=food_cat)
        context = {
            "form": form
        }
        return render(request, 'dashboard/food_cat_add.html', context)
    
    def post(self, request, *args, **kwargs):
        food_cat_id = kwargs["food_cat_id"]
        food_cat = FoodCategory.objects.get(id=food_cat_id)
        form = FoodCategoryForm(request.POST, instance=food_cat)
        if form.is_valid():
            form.save()
            return redirect('food_category_list')
        else:
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, 'dashboard/food_cat_add.html', context)
        
class FoodCategoryDeleteView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        food_cat_id = kwargs["food_cat_id"]
        food_cat = FoodCategory.objects.get(id=food_cat_id)
        food_cat.delete()
        return redirect('food_category_list')

class FeedbackView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        feedbacks = feedback.objects.all().order_by('-created_at')
        context={
            "feedbacks": feedbacks
        }


        return render(request, 'dashboard/feedback.html', context)
    