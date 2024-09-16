from django.urls import path
from . import views


app_name = 'trivia'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('suggest/', views.suggest, name='suggest'),
]