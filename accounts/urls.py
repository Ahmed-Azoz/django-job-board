from django.urls import path
from .import views
app_name='accounts' #lazem tktp asm al app

urlpatterns = [
    path('signup', views.signup, name='signup'),
]