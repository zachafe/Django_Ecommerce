#Importar librerias
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.utils.decorators import method_decorator
#Importar modelos
from app.erp.models import *
#vistas basadas en funciones
def category_list(request):
    data = {
        'title':'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request,'category/list.html',data)

#VISTA BASADAS EN CLASES
class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return Category.objects.all()
        #return Category.objects.filter(name__startswith='A')
    
    #editar el comportamiento
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de categorias'
        context["categories"]= context["object_list"]
        return context
    