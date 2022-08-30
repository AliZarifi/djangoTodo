from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    disc=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dateComplete=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.title