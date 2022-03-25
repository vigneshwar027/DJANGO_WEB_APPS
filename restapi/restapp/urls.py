from django.urls import path,include
from restapp import views



urlpatterns = [
    path('createuser/',views.CreateUserView.as_view(),name='create_user'), 
    path('item/',views.item,name='item'), 

]

    