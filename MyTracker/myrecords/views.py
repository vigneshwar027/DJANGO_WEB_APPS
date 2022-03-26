from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, auth


# Create your views here.

def home(request):
    return render(request,'login.html')

def dashboard(request):
    User = request.user
    profile = Student.objects.get(user = User)
    data = Test.objects.filter(student__user = User)    
    return render(request,'dashboard.html',{'data':data,'profile':profile})
