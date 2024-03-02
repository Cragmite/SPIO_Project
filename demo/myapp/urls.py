from django.urls import path
from . import views
from .views import MachineListView, selected_machine

urlpatterns = [
    path("", views.home, name="home")
]

urlpatterns = [
    path('machine-list/', MachineListView.as_view(), name='machine_list'),
    path('selected-machine/', selected_machine, name='selected_machine'),
]