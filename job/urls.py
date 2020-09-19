from django.urls import path
from .import views
from .import api
app_name='job' #lazem tktp asm al app

urlpatterns = [
    path('', views.job_list, name='job_List'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),

    ## api
    path('api/jobs', api.jobListapi, name='jobListapi'),
    path('api/jobs/<int:id>', api.job_details_api, name='job_details_api'),

    ## class based view
    path('api/v2/jobs', api.JobListApi.as_view(), name='JobListApi'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='JobDetail'),

]