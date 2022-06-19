from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
