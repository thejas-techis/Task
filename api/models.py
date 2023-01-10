from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
  sceduled_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
      
  def __str__(self):
    return self.title