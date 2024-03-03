from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('tickets/', views.getTickets),
    path('tickets/create/', views.createTicket),
    path('tickets/<str:pk>/update/', views.updateTicket),
    path('tickets/<str:pk>/delete/', views.deleteTicket),
    path('tickets/<str:pk>/', views.getTicket)
]