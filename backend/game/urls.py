from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_game, name='start_game'),
    path('submit/', views.submit_score, name='submit_score'),
    path('highscores/', views.high_scores, name='high_scores'),
    path('register/', views.register_user, name='register_user'),
]
