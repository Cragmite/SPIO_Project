from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('machines/', views.getMachines),
    path('machines/create/', views.createMachine),
    path('machines/<str:pk>/update/', views.updateMachine),
    path('machines/<str:pk>/delete/', views.deleteMachine),
    path('machines/<str:pk>/', views.getMachine)
]