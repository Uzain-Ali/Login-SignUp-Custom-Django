from django.shortcuts import render, redirect
from django.contrib import messages
from register_app.models import register

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = register.objects.get(email=email, password=password)
            messages.success(request, "Login successful!")
            return render(request,'login_page.html')
        except register.DoesNotExist:
            messages.error(request, "Invalid credentials! Please try again.")
            return render(request, 'login_page.html')
    else:
        return render(request, 'login_page.html')
