from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):

    form = UserRegistrationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account is created, now you can log in!')
            return redirect('login')
    context = {
        "form":form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile_view(request):
   
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account is updated succesfully!")
            return redirect("users:profile")

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        "user_form":user_form,
        "profile_form":profile_form
    }

    return render(request, "users/profile.html", context)



