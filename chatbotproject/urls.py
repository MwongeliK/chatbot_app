"""
URL configuration for chatbotproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from chatbot_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'), 
    path('login', views.login_view, name='login'),
    path('Home/', views.home, name='Home'),
    path('Dashboard/', views.dashboard, name='Dashboard'),
    path('chat/', views.chat, name='chat'),
    path('quiz/', views.quiz, name='quiz'),
    path('profile/', views.profile, name='profile'),
    path('modules/', views.modules , name= 'Modules'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'), 
    path('', include('chatbot_app.urls')),

    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='password_reset'),

    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
         name='password_reset_confirm'),

    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name='password_reset_complete'),
]


