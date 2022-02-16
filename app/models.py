from django.db import models
#from django.conf import settings
#IMPOTAR MODELO USER DEFAULT
#from django.contrib.auth.models import User
#IMPORTA MODELO USER PERSONALIZADO
#from app.user.models import User
from ecommerce.settings import *

#CLASE DE AUDITORIA, PARA LOS MODELOS QUE QUIERAN HEREDAR ESTOS CAMPOS
class BaseModel(models.Model):
    
    # user_creation = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_creation',null=True,blank=True)
    # date_creation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # user_updated = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_updated',null=True,blank=True)
    # date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    #PARA PODERLO UTILIZAR EN TODOS LOS MODELOS, CUANDO PERSONALIZADO EL USER A TRAVES DE UN MODELO PERSONALIZADO
    user_creation = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='%(app_label)s_%(class)s_creation',null=True,blank=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user_updated = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='%(app_label)s_%(class)s_updated',null=True,blank=True)
    date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    #FINAL CUANDO NO TENGO PERSONALIZADO EL MODELO USER
    #user_creation = models.ForeignKey(User,on_delete=models.PROTECT,related_name='%(app_label)s_%(class)s_creation',null=True,blank=True)
    #date_creation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    #user_updated = models.ForeignKey(User,on_delete=models.PROTECT,related_name='%(app_label)s_%(class)s_updated',null=True,blank=True)
    #date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        #PARA QUE EL OTRO MODELO HEREDE LOS CAMBPOS Y O SE IMPLEMENTE BASE MODEL EN LA DBA
        abstract = True