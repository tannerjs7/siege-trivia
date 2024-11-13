from django.urls import path
from . import views


app_name = 'trivia'
urlpatterns = [
    path('', views.index, name='index'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('suggest/', views.suggest, name='suggest'),
    path('questions/', views.questions, name='questions'),
]