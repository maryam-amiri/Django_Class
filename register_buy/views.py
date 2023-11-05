from django.contrib.auth import logout
from django.db.models import Avg, Max, Min
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import CourseRegister


def register_buy(request):
    CourseRegisters = CourseRegister.objects.all()
    context = {
        'CourseRegister': CourseRegisters,
    }
    return render(request, 'register_buy/register_courses.html',context)


def user_logout(request):
    logout(request)
    return redirect('home_module:home')

