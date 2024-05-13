from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from app.models import register
from .middlewares import auth, guest


def home(request):
    return render(request, 'home.html')


@guest
def signup_view(request):
    if(request.method=="POST"):
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('gender') and request.POST.get('password'):
            saverecord = register()
            saverecord.fname = request.POST.get('fname')
            saverecord.lname = request.POST.get('lname')
            saverecord.email = request.POST.get('email')
            saverecord.gender = request.POST.get('gender')
            saverecord.password = request.POST.get('password')
            saverecord.save()
            messages.success(request, "User Added..")
            return redirect('login')
    else:
            return render(request,'signup_page.html')


@guest
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = register.objects.get(email=email, password=password)
            messages.success(request, "Login successful!")  
            return redirect('home')
        except register.DoesNotExist:
            messages.error(request, "Invalid credentials! Please try again.")
            return render(request, 'login_page.html')
    else:
        return render(request, 'login_page.html')

@auth
def logout_view(request):
    logout(request)
    return redirect('login')