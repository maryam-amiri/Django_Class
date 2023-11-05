from django.urls import path

from . import views

app_name='courses'

urlpatterns = [
    path('course',views.all_courses,name='courses'),

]

