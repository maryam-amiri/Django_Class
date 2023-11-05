from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class CourseRegister(models.Model):
    title=models.CharField(max_length=50,verbose_name='name of course')
    descriptionCourse=models.CharField(max_length=300,default='')



