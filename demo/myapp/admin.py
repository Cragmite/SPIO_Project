from django.contrib import admin
from .models import TodoItem
from .models import Machine

# Register your models here.
admin.site.register(Machine)
admin.site.register(Failure)
admin.site.register(Ticket)