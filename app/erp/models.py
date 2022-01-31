from django.db import models
from datetime import datetime
from django.forms import model_to_dict
#IMPOTAR MODELO USER
from django.contrib.auth.models import User
#IMPORTAR LOS choices PARA las opciones
from app.erp.choices import *

#LIBRERIA DE HISTORICO
from simple_history.models import HistoricalRecords
#LIBRERIA CRUM
from crum import get_current_user
#IMPORTAR MODELO BASE  PARA CAMPOS DE AUDITORIA
from app.models import BaseModel

from ecommerce.settings import MEDIA_URL, STATIC_URL

class Type (models.Model):
    name = models.CharField(max_length=150,unique=True,verbose_name='Nombre')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ='Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Category (models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre',unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')
    
    def __str__(self):
        return self.name
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
        
    class Meta:
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Employee(BaseModel):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type,on_delete=models.PROTECT)
    names = models.CharField(max_length=150,verbose_name='Nombres')
    lastname = models.CharField(max_length=150,verbose_name='Apellidos')
    dni = models.CharField(max_length=10,unique=True,verbose_name='Identificacion')
    date_joined = models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True,verbose_name='Fecha de creacion')
    date_updated = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de actualizacion')
    age = models.PositiveIntegerField(default=0,verbose_name='Edad')
    salary = models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name='Salario')
    state = models.BooleanField(default=True,verbose_name='Estado')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d',null=True,blank=True)
    sex = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False,verbose_name='Sexo')
    
    #GENERAR HISTORICO A LA TABLA
    historical = HistoricalRecords()

    #para la parte de historico
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    #SOBREESCRIBIR MODELO SAVE PARA CAMPOS DE CONTROL
    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Employee,self).save()
    
    #Representacion del objeto
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table ='empleado'
        ordering = ['id']
        
class Product(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT,verbose_name='Categoria')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True,verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,verbose_name='Precio de Venta')

    #GENERAR HISTORICO A LA TABLA
    historical = HistoricalRecords()

    #para la parte de historico
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    #SOBREESCRIBIR MODELO SAVE PARA CAMPOS DE CONTROL
    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Product,self).save()
    
    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Client(BaseModel):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=10, choices=SEXO_CHOICES, default='M', verbose_name='Sexo')

    #GENERAR HISTORICO A LA TABLA
    historical = HistoricalRecords()

    #para la parte de historico
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    #SOBREESCRIBIR MODELO SAVE PARA CAMPOS DE CONTROL
    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Client,self).save()
    
    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = self.get_gender_display()
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
        
class Sale(BaseModel):
    cli = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    #GENERAR HISTORICO A LA TABLA
    historical = HistoricalRecords()

    #para la parte de historico
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    #SOBREESCRIBIR MODELO SAVE PARA CAMPOS DE CONTROL
    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Sale,self).save()
    
    def __str__(self):
        return self.cli.names
        
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(BaseModel):
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT)
    prod = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    #GENERAR HISTORICO A LA TABLA
    historical = HistoricalRecords()

    #para la parte de historico
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    #SOBREESCRIBIR MODELO SAVE PARA CAMPOS DE CONTROL
    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(DetSale,self).save()

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
    
    