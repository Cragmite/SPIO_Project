from django.db import models

# Create your models here.

class Machine(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.name

        
class Failure(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True)
    failure = models.ForeignKey(Failure, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return  str(self.id)
        return  self.description[0:50]
    
    class Meta:
        ordering = ['-updated']