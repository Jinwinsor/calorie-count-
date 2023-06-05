from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.DecimalField(max_digits=100, decimal_places=1)
    protein = models.DecimalField(max_digits=100, decimal_places=1)
    fats = models.DecimalField(max_digits=100, decimal_places=1)
    calories = models.DecimalField(max_digits=100, decimal_places=1)

    def __str__(self):
        return self.name


class Intake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_intake = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
