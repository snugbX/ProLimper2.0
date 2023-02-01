from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendedores, name="vendedor"),
    path('delete_vendedor/<int:pk>/', views.delete_vendedor, name='del_Vendedor'),
    path('Atualiza_vendedor/<int:pk>/', views.update_vendedor, name='att_Vendedor'),
]
