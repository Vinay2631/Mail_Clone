from msilib.schema import Error
from multiprocessing import context
from django import forms
from django.http import HttpRequest
from vmail.models import Post
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registerd! Please register with different Mail')
                form=UserRegisterForm()
                return render(request, 'users/register.html', {'form': form})
            else:
                form.save()
                messages.success(request, f'Your account is created! You can login now!')
                return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account is updated')
            return redirect('/')
    else: 
        u_form=UserUpdateForm(instance=request.user)
    context={
        'u_form':u_form 
    }
    return render(request, 'users/profile.html',context)