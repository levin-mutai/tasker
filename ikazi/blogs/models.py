from django.db import models
from django.utils import timezone
import readtime,datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Blogs(models.Model):
    blog_id = models.BigAutoField(primary_key = True)
    blog_image = models.ImageField(upload_to='uploads')
    blog_title = models.CharField(max_length=100)
    blog_slug = models.CharField(max_length=100,default='')
    content = RichTextField(blank=True,null=True)
    views = models.IntegerField(default=0)
    rating = models.IntegerField(default=1)
    date_posted = models.DateField(default=timezone.now)
    minute_read = models.CharField(max_length=50,help_text="Minutes taken to read the blog. This will be auto-calculated, no need to fill it",default=str(readtime.of_text(content)))

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")
    # def __init__(self):
    #

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.minute_read = str(readtime.of_text(self.content))
        return super(Blogs,self).save(*args, **kwargs)
    def __str__(self):
        return self.blog_title


