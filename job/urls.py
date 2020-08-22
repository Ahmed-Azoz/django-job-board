from django.urls import path
from .import views
app_name='job' #lazem tktp asm al app

urlpatterns = [
    path('', views.job_list),
    path('', views.job_list_num, name='List'),

    path('<int:id>', views.job_detail, name='job_detail'),
]