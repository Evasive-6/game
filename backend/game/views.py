import random
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game, Score
from .serializers import GameSerializer, ScoreSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def start_game(request):
    colors = ['red', 'blue', 'green', 'yellow']
    sequence = [random.choice(colors) for _ in range(3)]  # Start with 3 colors
    game = Game.objects.create(sequence=sequence, level=1)
    serializer = GameSerializer(game)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def submit_score(request):
    user_id = request.data.get('user_id')
    game_id = request.data.get('game_id')
    score = request.data.get('score')

    if not all([user_id, game_id, score]):
        return Response({'error': 'Missing data'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
        game = Game.objects.get(id=game_id)
        Score.objects.create(user=user, game=game, score=score)
        return Response({'message': 'Score submitted'}, status=status.HTTP_201_CREATED)
    except (User.DoesNotExist, Game.DoesNotExist):
        return Response({'error': 'Invalid user or game'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def high_scores(request):
    scores = Score.objects.order_by('-score')[:10]
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not all([username, email, password]):
        return Response({'error': 'Missing data'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User created', 'user_id': user.id}, status=status.HTTP_201_CREATED)

# Add sample data for testing
@api_view(['POST'])
def add_sample_data(request):
    if not User.objects.exists():
        user = User.objects.create_user(username='sample', email='sample@example.com', password='password')
        game = Game.objects.create(sequence=['red', 'blue'], level=1)
        Score.objects.create(user=user, game=game, score=10)
    return Response({'message': 'Sample data added'})
