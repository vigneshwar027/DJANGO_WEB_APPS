from django.urls import path
from finder import views

urlpatterns = [    
    path('',views.home,name='home'),
]
