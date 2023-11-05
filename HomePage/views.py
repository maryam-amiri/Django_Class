from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from HomePage.forms import registerForm, UserLoginForm
from django.contrib.auth.decorators import login_required

from register_buy.models import CourseRegister


# from HomePage.forms import registerForm, UserLoginForm


# Create your views here.

def HomePage(request):
    return render(request,'HomePage/HomePage.html')




def register(request):
    if request.method == 'POST':
        form_register = registerForm(request.POST)
        if form_register.is_valid():
            data = form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password2'])
            form_register.save()
            return redirect('HomePage:login')
    else:
        form_register = registerForm()
    return render(request, 'HomePage/register.html', {'form_register': form_register})

#----------------------------function login:

def user_login(request):
    if request.method == 'POST':
        form_login=UserLoginForm(request.POST)
        if form_login.is_valid():
            data=form_login.cleaned_data
            try:
                user=authenticate(request,username=User.objects.get(email=data['user']),password=data['password'])
            except:
                user=authenticate(request,username=data['user'],password=data['password'])
            if user is not None:
                 login(request, user)
                 return redirect('HomePage:reg_buy')
    else:
        form_login = UserLoginForm()
    return render(request, 'HomePage/login.html', {'form_login': form_login})

@login_required
def register_buy(request):
    CourseRegisters = CourseRegister.objects.all()
    context = {
        'CourseRegister': CourseRegisters,
    }
    return render(request, 'register_buy/register_courses.html', context)





