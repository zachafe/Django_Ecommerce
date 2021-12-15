from django.db import models
from datetime import datetime

#LIBRERIA DE HISTORICO
from simple_history.models import HistoricalRecords
#LIBRERIA CRUM
from crum import get_current_user
#IMPORTAR MODELO BASE  PARA CAMPOS DE AUDITORIA
from app.models import BaseModel

# Create your models here.
class Employee(BaseModel):
    
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino")
    )
    
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