#Importar librerias
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse

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

    #@method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        data = {}
        #print(request.POST)
        try:
            #cat = Category.objects.get(pk=request.POST['id'])
            #data['name'] = cat.name
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_queryset(self):
        return Category.objects.all()
        #return Category.objects.filter(name__startswith='A')
    
    #editar el comportamiento
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de categorias'
        context["categories"]= context["object_list"]
        return context
    