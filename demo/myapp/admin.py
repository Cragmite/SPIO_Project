from django.contrib import admin
from .models import Machine
from .models import Failure
from .models import Ticket

# Register your models here.
admin.site.register(Machine)
admin.site.register(Failure)
admin.site.register(Ticket)