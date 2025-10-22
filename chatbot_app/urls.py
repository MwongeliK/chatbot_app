from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('Login/', views.login, name='Login'),
    path('Dashboard/', views.dashboard, name='Progress Dashboard'),
    path('chat/', views.chat, name='chatbot'),
    path('quiz/', views.quiz, name='quiz'),
    path('profile/', views.profile, name='profile'),
]
