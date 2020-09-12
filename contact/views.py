from django.shortcuts import render
from .models import info
# Create your views here.
def send_massage(request):
    myinfo = info.objects.first
    return render(request, 'contact/contact.html', {'myinfo': myinfo})