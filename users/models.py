from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    about_me = models.TextField()
    firstName = models.CharField(max_length = 20, unique = False, default="")
    lastName = models.CharField(max_length = 20, unique = False, default="")
    school = models.CharField(max_length = 100, default = "")
    links = models.TextField()
    image = models.ImageField(upload_to='profile', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
