"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
#importar vistas
#from app.erp.views import *
from app.erp.views.category.views import *
from app.erp.views.dashboard.views import *
from app.erp.views.product.views import *
#agrupar mi listas
app_name='erp'

urlpatterns = [
    # path('uno/',myFirstView,name='vista1'),
    # path('dos/',mySecondView,name='vista2'),
    # path('tres/',myFirstModel,name='vista3'),
    # path('productos/',myFirstProductos,name='productos'),
    #path('category/list/',category_list,name='category_list_function'),
    path('category/list/',CategoryListView.as_view(),name='category_list'),
    #path('category/listClass2/',CategoryListView.as_view(),name='category_list2'),
    path('category/add/',CategoryCreateView.as_view(),name='category_create'),
    path('category/update/<int:pk>/',CategoryUpdateView.as_view(),name='category_update'),
    path('category/delete/<int:pk>/',CategoryDeleteView.as_view(),name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
