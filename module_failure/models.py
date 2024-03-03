from django.db import models

# Create your models here.

class Failure(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name