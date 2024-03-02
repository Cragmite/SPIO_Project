from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Machine(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.name