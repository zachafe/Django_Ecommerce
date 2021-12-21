#Importar librerias
from django.shortcuts import render
#Importar modelos
from app.erp.models import *
#vistas basadas en funciones
def category_list(request):
    data = {
        'title':'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request,'category/list.html',data)
