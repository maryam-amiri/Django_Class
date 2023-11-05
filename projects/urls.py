from django.urls import path

from . import views

app_name='Projects'

urlpatterns = [
    path('projects',views.OurProjects,name='projects')
]