from django.shortcuts import render
import mysql.connector as sql
from register_app.models import register
from django.contrib import messages

# Create your views here.
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
            return render(request,'signup_page.html')
    else:
            return render(request,'signup_page.html')
