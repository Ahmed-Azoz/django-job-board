from django.urls import path
from .import views
app_name='job' #lazem tktp asm al app

urlpatterns = [
    path('', views.job_list, name='List'),
    path('/add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
]