from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    email = models.CharField(max_length=100,error_messages={"unique":"Email Already Exists"})
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})