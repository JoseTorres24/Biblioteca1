from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('listar_libros/', views.listar_libros, name='listar_libros'),
    path('registrar_libro/', views.registrar_libro, name='registrar_libro'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('listar_prestamos/', views.listar_prestamos, name='listar_prestamos'),
]
