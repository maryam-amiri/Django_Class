from django.db import models

# Create your models here.
class ContactUs(models.Model):
    title=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    name=models.CharField(max_length=300)
    message=models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='contact us'
        verbose_name_plural='list of contact us'


