from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, "AppIntermedio/index.html")


def libros(request):
    return render(request,"libros/index.html")

def inicio(request):
    return render(request,"AppIntermedio/inicio.html")

