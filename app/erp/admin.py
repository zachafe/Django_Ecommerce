from django.contrib import admin

# Register your models here.
from app.erp.models import *


#PERSONALIZAR CENTRAL PARA MOSTRAR EN EL ADMIN
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name','cat')
    list_display = ('name','cat','pvp','image','user_creation','date_creation')
    
#REGISTRAR MODELOS
Category
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
