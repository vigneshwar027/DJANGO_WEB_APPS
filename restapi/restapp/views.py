from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from restapp import serializers
from .serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.contrib.auth.models import User

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny,)    
    serializer_class = UserSerializer


def he

def item(request):
    tasks = Task.objects.all()
    return render(request,'item.html',{"tasks":tasks})