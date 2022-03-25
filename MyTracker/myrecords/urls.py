from django.urls import path
from myrecords import views

urlpatterns = [
    path('',views.home,name='home'),
]


