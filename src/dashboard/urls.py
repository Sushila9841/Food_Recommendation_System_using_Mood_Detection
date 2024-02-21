from django.urls import path
from .views import *
from frontend.views import *

urlpatterns = [
    path('', DashBoardView.as_view(), name='dashboard'),
    path('logout', LogoutView.as_view(), name="logout"),
    path('food_list', FoodListView.as_view(), name="food_list"),
    path('food/add', FoodAddView.as_view(), name="food_add"),
    path('food/edit/<int:food_id>', FoodEditView.as_view(), name="food_edit"),
    path('food/delete/<int:food_id>', FoodDeleteView.as_view(), name="food_delete"),
    path('food/category_list', FoodCategoryListView.as_view(), name="food_category_list"),
    path('food/category/add', FoodCategoryAddView.as_view(), name="food_category_add"),
    path('food/category/edit/<int:food_cat_id>', FoodCategoryEditView.as_view(), name="food_category_edit"),
    path('food/category/delete/<int:food_cat_id>', FoodCategoryDeleteView.as_view(), name="food_category_delete"),
    path('food/feedback', FeedbackView.as_view(), name="feedback")
 
]
