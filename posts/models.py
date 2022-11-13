from django.db import models

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=100, blank=False)
    content = models.TextField()
    author = models.TextField(max_length=100, blank=False)

    class Meta:
        ordering = ['created']
