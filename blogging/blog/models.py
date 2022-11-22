from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Model
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='images/profile/')
    facebook =models.CharField(max_length=100,default='code')
    twitter = models.CharField(max_length=100,default='code')
    instagram = models.CharField(max_length=100,default='code')

    def __str__(self):
        return str(self.user)


class Member(models.Model):
    title = models.CharField(max_length=100)
    blog_image=models.ImageField(blank=True,null=True,upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField(max_length=100)
    body = RichTextField(blank=True,null=True)
    post_date=models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    snippet = models.CharField(max_length=100)
    likes=models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
