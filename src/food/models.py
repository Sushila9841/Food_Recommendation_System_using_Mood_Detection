from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User




class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Food Categories'
    def __str__(self):
        return self.name
    



class Food(models.Model):
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='food_images')
    urls = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


class MoodVsFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)
    food = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " " + self.mood + " " + self.food.name
    