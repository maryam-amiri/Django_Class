from django.http import JsonResponse
from django.shortcuts import render

from .models import course


# Create your views here.

def all_courses(request):
    courses = course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'course/course.html',context)


