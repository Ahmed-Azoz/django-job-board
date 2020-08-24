from django.shortcuts import render
from .models import job
from django.core.paginator import Paginator
from .models import Apply
# Create your views here.

def job_list(request):
    job_list = job.objects.all()

    paginator = Paginator(job_list, 1) # Show 1 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = { 'jobs' : page_obj}
    return render(request, 'job/job_list.html', context)

# def job_list_num(request):
#     job_list = job.objects.all()

#     # context = { 'List' : job_list}
#     return 'count(job_list)'

def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug)
    if request.method == 'POST':
        pass
    else:
        form = Applyform()



    context = {'job': job_detail, 'form':form }
    return render(request, 'job/job_detail.html',context)