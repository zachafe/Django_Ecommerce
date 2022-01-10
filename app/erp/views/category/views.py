#Importar librerias
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect

#Importar modelos
from app.erp.models import *
#importar formularios
from app.erp.forms import CategoryForm

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
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    # def post(self,request, *args, **kwargs):
    #     data = {}
    #     #print(request.POST)
    #     try:
    #         #cat = Category.objects.get(pk=request.POST['id'])
    #         #data['name'] = cat.name
    #         data = Category.objects.get(pk=request.POST['id']).toJSON()
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)
    
    def get_queryset(self):
        return Category.objects.all()
        #return Category.objects.filter(name__startswith='A')
    
    #editar el comportamiento, object_list esta la data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = 'Listado de categorias'
    #     context["categories"]= context["object_list"]
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        return context

#VISTA BASADA EN CLASES CREAR
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #     print(request.POST)
    #     form = CategoryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'add'
        return context

#VISTA BASADA EN CLASES UPDATE
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')
    
    def dispatch(self, request, *args, **kwargs):
        #OBTENER EL OBJETO ACTUAL QUE ESTAMOS LLAMANDO POR AJAX
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        #print(self.object)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'edit'
        return context

#VISTA BASADA EN CLASES DELETE
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('erp:category_list')
    
    #OBTENER EL OBJETO
    #@method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        #print(self.object)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'delete'
        return context