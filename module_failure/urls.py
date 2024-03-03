from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('failures/', views.getFailures),
    path('failures/create/', views.createFailure),
    path('failures/<str:pk>/update/', views.updateFailure),
    path('failures/<str:pk>/delete/', views.deleteFailure),
    path('failures/<str:pk>/', views.getFailure)
]