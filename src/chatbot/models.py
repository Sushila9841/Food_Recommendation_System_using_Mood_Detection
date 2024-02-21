from django.db import models

class FoodRecommendation(models.Model):
    mood = models.CharField(max_length=20)
    food = models.TextField()

    def __str__(self):
        return self.mood
