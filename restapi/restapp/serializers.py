from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','password']


class TaskSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None,use_url=True)

    # in video session they are adding image field in this py files like with above code..
    # i dont understand since it is not neccessary    

    class Meta:
        model = Task
        fields='__all__'

