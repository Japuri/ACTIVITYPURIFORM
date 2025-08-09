from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_tweet, name='create_tweet'),
    path('success/', views.tweet_success, name='tweet_success'),
]
