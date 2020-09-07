from django.shortcuts import redirect, render
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')

    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
    else:
        userform = UserForm(instance=request.user)
        # 3shan tbase l date ll form
        profileform = ProfileForm(instance=profile) 
    return render(request,'accounts/profile_edit.html',{'userform':userform, 'profileform':profileform})
