from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)

class TrashModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)

class CompleteModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
