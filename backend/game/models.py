from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    sequence = models.JSONField()  # List of colors, e.g., ['red', 'blue', 'green']
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
