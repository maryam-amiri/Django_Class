from django.db import models

# Create your models here.


class course(models.Model):
    title=models.CharField(max_length=50,verbose_name='name of course')
    description=models.CharField(max_length=300,verbose_name='description',default='')



