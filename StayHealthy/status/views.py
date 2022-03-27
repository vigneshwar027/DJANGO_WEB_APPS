from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, auth
# Create your views here.


def status(request):
    User = request.user     
    treatment = Treatment.objects.filter(patient__user = User,completion = True)
    return render(request,'status.html',{'treatment':treatment})