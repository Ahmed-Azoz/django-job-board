from django.shortcuts import redirect, render
from .models import job
from django.core.paginator import Paginator
from .form import Applyform, jobform
from django.urls import reverse
# Create your views here.

def job_list(request):
    job_list = job.objects.all()

    paginator = Paginator(job_list, 2) # Show 1 contacts per page.
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
        form = Applyform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            form.save()
    else:
        form = Applyform()



    context = {'job': job_detail, 'form1':form }
    return render(request, 'job/job_detail.html',context)



def add_job(request):
    if request.method == 'POST':
        form = jobform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_List'))
    else:
        form = jobform()

    return render(request, 'job/add_job.html', {'form': form})
