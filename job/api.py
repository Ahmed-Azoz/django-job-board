### view(function)
from .models import job
from .serializers import JobSerializer #bt3ml serialize ll data l rag3a kolha
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def jobListapi(request):
    all_jobs = job.objects.all()
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data':data})




@api_view(['GET'])
def job_details_api(request, id):
    job_detail = job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data':data})



class JobListApi(generics.ListAPIView):
    model = job
    queryset = job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = job.objects.all()

    lookup_field = 'id'
