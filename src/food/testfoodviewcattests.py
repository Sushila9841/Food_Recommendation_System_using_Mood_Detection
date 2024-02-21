from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from food.models import FoodCategory  # Import the FoodCategory model

class TestFoodCategoryListView(TestCase):

    def test_food_category_list_view_with_existing_categories(self):
        # Create sample food categories for testing
        FoodCategory.objects.create(name='Category A')
        FoodCategory.objects.create(name='Category B')

        # Make a GET request to the food category list view
        response = self.client.get(reverse('food_category_list'))  # Replace 'food_category_list' with your actual URL name

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the food categories are displayed in the response content (customize based on your template)
        self.assertContains(response, 'Category A')  # Replace 'Category A' with the actual category name
        self.assertContains(response, 'Category B')  # Replace 'Category B' with the actual category name

    def test_food_category_list_view_with_no_categories(self):
        # Make a GET request to the food category list view when there are no categories
        response = self.client.get(reverse('food_category_list'))  # Replace 'food_category_list' with your actual URL name

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that a message indicating no categories is displayed in the response content
        self.assertContains(response, 'No categories available')  # Customize based on your template

    # Add more black-box test cases for other views as needed
