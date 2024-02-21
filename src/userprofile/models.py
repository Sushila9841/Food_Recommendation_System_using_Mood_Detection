from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField(null = True, blank = True)
    phone_number = models.CharField(max_length=10, null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    gender = models.CharField(max_length=10, null = True, blank = True)
    has_filled_survey = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
    
class MoodHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " " + self.mood + " " + str(self.date)
    