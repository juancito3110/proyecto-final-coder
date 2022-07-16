from django.shortcuts import render

# Create your views here.



def libros(request):
    return render(request,"libros/index.html")

def inicio(request):
    return render(request,"AppIntermedio/inicio.html")

def crear(request):
    return render(request,"libros/crear.html") 

def editar(request):
    return render(request,"libros/editar.html")

def ubicacion(request):
    return render(request, "ubicacion/buscar.html")

def buscar(request):
    return render(request, "ubicacion/buscar.html")

def contacto(request):
    return render(request, "contacto/contacto.html")

def datoscontacto(request):
    return render(request, "contacto/contacto.html")
