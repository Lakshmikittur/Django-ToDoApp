from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=False)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('tasks:taskdetail', kwargs = {"id":self.id})