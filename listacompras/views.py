from django.shortcuts import render
from django.utils import timezone
from .models import Producto

def index(request):
    producto = Producto.objects.order_by('Fecha_de_Compra')
    return render(request, 'listas/index.html', {'producto': producto})