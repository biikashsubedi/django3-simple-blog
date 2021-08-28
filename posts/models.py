import uuid

from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(null=True, blank=True, default='posts.png', upload_to='images')
    content = models.TextField()
    createdBy = models.CharField(null=True, blank=True, max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name_plural = 'Post'

    def get_absolute_url(self):
        return reverse('single.post', kwargs={'id': self.id})
