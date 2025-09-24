from rest_framework import serializers
from .models import Game, Score
from django.contrib.auth.models import User

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'sequence', 'level', 'created_at']

class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    game = GameSerializer()

    class Meta:
        model = Score
        fields = ['id', 'user', 'game', 'score', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
