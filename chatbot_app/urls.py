from django.urls import path
from .import views

urlpatterns = [

    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'), 
    path('home/', views.home, name='home'),
    path('Dashboard/', views.dashboard, name='Dashboard'),
    path('chat/', views.chat, name='chat'),
    path('quiz/', views.quiz, name='quiz'),
    path('profile/', views.profile, name='profile'),
    path('modules/', views.modules, name='modules'),
    path('logout/', views.logout_view, name='logout'),
     path('register/', views.register_view, name='register'), 

]
