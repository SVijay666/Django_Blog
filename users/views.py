from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        userup_form = UserUpdateForm(request.POST , instance = request.user)
        profileup_form = ProfileUpdateForm(request.POST , request.FILES , instance = request.user.profile)
        if userup_form.is_valid() and profileup_form.is_valid():
            userup_form.save()
            profileup_form.save()
            messages.success(request, f'Your account has been updated with new information')
            return redirect('Profile')
    else:
        userup_form = UserUpdateForm(instance = request.user)
        profileup_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'user_update_form' : userup_form,
        'profile_update_form' : profileup_form
    }
    return render(request, 'users/profile.html' , context)