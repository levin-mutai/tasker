from django.db import models
from rest_framework import serializers
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.  

class categories(models.Model):
    jcategory = models.CharField(max_length=50,primary_key=True)

    class Meta:
        verbose_name = ("Job category")
        verbose_name_plural = ("Job categories")

    def __str__(self):
        return self.jcategory


class job (models.Model):
    types = (
        ('Intern', 'Intern'),
        ('Part-time', 'Part-time'),
        ('Remote', 'Remote'),
        ('Full-time', 'Full-time'),
        ('Hybrid', 'Hybrid')
    )
    job_id = models.AutoField(primary_key = True)
    job_title = models.CharField( max_length=150, blank = False)
    job_type =  models.CharField(max_length=150,choices=types)
    company = models.CharField(max_length=50,blank = False)
    Company_logo = models.ImageField(upload_to ='logos/% Y/% m/% d/')
    location = models.CharField( max_length=50)
    experience = models.CharField(max_length=250)
    category = models.ForeignKey("categories",on_delete=models.CASCADE)
    job_description = RichTextField(blank=True,null=True)
    # daysPublished = models.
    date_posted = models.DateField(default=timezone.now)
    # def __init__(self):
    #     date_posted = self.date_posted
    def __str__(self):
        return self.job_title