from django.db import models
#from django.conf import settings
#IMPOTAR MODELO USER
from django.contrib.auth.models import User

#CLASE DE AUDITORIA, PARA LOS MODELOS QUE QUIERAN HEREDAR ESTOS CAMPOS
class BaseModel(models.Model):
    
    # #user_creation = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_creation',null=True,blank=True)
    # date_creation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # #user_updated = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_updated',null=True,blank=True)
    # date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    # #PARA PODERLO UTILIZAR EN TODOS LOS MODELOS Y COMO VAN A REFERENCIAR A UNA CLASE DEBO GARANTIZAR QUE EL related_name SEA UNICO
    # user_creation = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_creation',null=True,blank=True)
    # user_updated = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_updated',null=True,blank=True)
    
    #FINAL
    user_creation = models.ForeignKey(User,on_delete=models.PROTECT,related_name='%(app_label)s_%(class)s_creation',null=True,blank=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user_updated = models.ForeignKey(User,on_delete=models.PROTECT,related_name='%(app_label)s_%(class)s_updated',null=True,blank=True)
    date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        #PARA QUE EL OTRO MODELO HEREDE LOS CAMBPOS Y O SE IMPLEMENTE BASE MODEL EN LA DBA
        abstract = True