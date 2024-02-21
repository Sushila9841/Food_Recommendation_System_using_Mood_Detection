from django.test import TestCase
from django.urls import reverse
from food.models import Food  # Import the Food model

class TestFoodListView(TestCase):

    def test_food_list_view_with_existing_food(self):
        # Create a sample food object for testing
        Food.objects.create(name='Test Food', description='Sample description', price=10.99)

        # Make a GET request to the food list view
        response = self.client.get(reverse('food_list'))  # Replace 'food_list' with your actual URL name

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the food item is displayed in the response content (customize based on your template)
        self.assertContains(response, 'Test Food')  # Replace 'Test Food' with the actual food name

    def test_food_list_view_with_no_food(self):
        # Make a GET request to the food list view when there are no food items
        response = self.client.get(reverse('food_list'))  # Replace 'food_list' with your actual URL name

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that a message indicating no food items is displayed in the response content
        self.assertContains(response, 'No food items available')  # Customize based on your template

    # Add more black-box test cases for other views as needed
