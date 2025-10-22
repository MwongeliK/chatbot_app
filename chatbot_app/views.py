from django.shortcuts import render

# Create your views here
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def admin(request):
    return render(request, 'admin.html')

def chat(request):
    return render(request, 'chat.html')

def quiz(request):
    return render(request, 'quiz.html')

def profile(request):
    return render(request, 'profile.html')


