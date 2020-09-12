from django.urls import path
from .import views
app_name='contact' #lazem tktp asm al app

urlpatterns = [
    path('', views.send_massage, name='contact'),
]