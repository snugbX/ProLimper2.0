
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/' , include('clientes.urls')),
    path('' , include('home.urls')),
    path('vendedor/' , include('vendedor.urls')),
]
