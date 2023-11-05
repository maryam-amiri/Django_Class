from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=300)
    url_title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class ProductInformation(models.Model):
    color=models.CharField(max_length=200)
    size=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.color}----{self.size}'




class ProductTag(models.Model):
    tag=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.tag}'



class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True,verbose_name='دسته بندی')
    product_information=models.OneToOneField(ProductInformation,on_delete=models.CASCADE,null=True,blank=True,verbose_name='اطلاعات تکمیلی',related_name='product_info')
    product_tag=models.ManyToManyField(ProductTag)
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=300)
    is_active=models.BooleanField()
    ratings=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)])
    slug=models.SlugField(max_length=400,unique=True,default='',null=False,db_index=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}--{self.description}--{self.price}'

    def get_absolute_url(self):
        return reverse('product:product_details',args={self.slug})


