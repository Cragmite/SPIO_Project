from django.db import models
from module_machine import models as models_machine
from module_failure import models as models_failure

# Create your models here.
        
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    machine = models.ForeignKey(models_machine.Machine, on_delete=models.CASCADE, null=True)
    failure = models.ForeignKey(models_failure.Failure, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return  str(self.id)
        return  self.description[0:50]
    
    class Meta:
        ordering = ['-updated']