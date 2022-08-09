#from asyncio.windows_events import NULL
from urllib import request
from email.policy import default
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify


All = 'all'

lvl = (
    (100, "100 Level"),
    (200, "200 Level"),
    (300, "300 Level"),
    (400, "400 Level"),
    (500, "500 Level"),
    (000, "Not specific"),
) 



class Post(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    #level = models.IntegerField(choices = lvl, default = 000)
    #school = models.CharField(max_length = 100, unique = False)#should not be unique
    #course_code = models.CharField(max_length = 20, unique = False)#sgould not be unique
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(default="no desc")
    uploaded_on = models.DateTimeField(auto_now_add = True)
    Book_author = models.CharField(max_length = 100, unique = False)#should not be unique
    #rating = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)])
    #uploaded_by = models.ForeignKey(User, on_delete = models.CASCADE,related_name='blog_posts')
    uploaded_by = models.ForeignKey(User, related_name="uploaded_by", on_delete = models.CASCADE,)
    views = models.IntegerField(default=0)
    file = models.FileField(upload_to = "books/%y/%m/%d")
    thumbnail = models.FileField(upload_to= "thumb/%y/%m/%d", default="")
	
	
    class Meta:
	    ordering = ['-uploaded_on']



    def __str__(self):
        return self.title

    