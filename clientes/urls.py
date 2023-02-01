from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('delete_cliente/<int:pk>/', views.delete_cliente, name='delCliente'),
    path('att_Cliente/<int:pk>/', views.update_cliente, name='att_Cliente'),
]
