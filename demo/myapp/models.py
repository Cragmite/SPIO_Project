from django.db import models

# Create your models here.

class Machine(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=255)

        
class Failure(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)


class Ticket(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)