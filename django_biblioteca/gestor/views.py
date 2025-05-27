from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from .models import Libro, Usuario, Prestamo

def menu(request):
    return render(request, 'gestor/menu.html')

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestor/listar_libros.html', {'libros': libros})

def registrar_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        genero = request.POST['genero']
        año_publicacion = request.POST['año_publicacion']
        disponible = 'disponible' in request.POST
        Libro.objects.create(
            titulo=titulo, autor=autor, genero=genero, año_publicacion=año_publicacion, disponible=disponible
        )
    return render(request, 'gestor/registrar_libro.html')

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        numero_identificacion = request.POST['numero_identificacion']
        Usuario.objects.create(nombre=nombre, email=email, numero_identificacion=numero_identificacion)
    return render(request, 'gestor/registrar_usuario.html')

def listar_prestamos(request):
    prestamos = Prestamo.objects.select_related('usuario', 'libro').all()
    usuarios = Usuario.objects.all()
    libros = Libro.objects.filter(disponible=True)
    if request.method == 'POST':
        usuario_id = request.POST['usuario']
        libro_id = request.POST['libro']
        Prestamo.objects.create(
            usuario_id=usuario_id,
            libro_id=libro_id,
        )
        libro = Libro.objects.get(id=libro_id)
        libro.disponible = False
        libro.save()
    return render(request, 'gestor/listar_prestamos.html', {'prestamos': prestamos, 'usuarios': usuarios, 'libros': libros})

