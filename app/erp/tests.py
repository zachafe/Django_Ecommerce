from ecommerce.wsgi import *
from app.erp.models import Type, Employee

# LISTAR
# query = Type.objects.all()
# print(query)

# INSERTAR
# t = Type()
# t.name = 'Operario'
# t.save()

# EDITAR
# t = Type.objects.get(pk=3)
# t.name = 'Operario Auxiliar 1'
# t.save()

# ELIMINAR
# t = Type.objects.get(pk=1)
# t.delete()

#EXEPCIONES
# try:
#     t = Type.objects.get(pk=1)
#     print(t)
# except Exception as e:
#     print(e)

#LISTAR UTILIZANDO FILTROS
#name__contains = LIKE
obj = Type.objects.filter(name__contains='Presidente')
#TOMAR MINUSCULA Y MAYUSCULAS
obj = Type.objects.filter(name__icontains='Presidente')
#IN
obj = Type.objects.filter(name__in =['Accionista','Presidente']).count()
#REGEXP
obj = Type.objects.filter(name__iregex ='Aux')
#NO INT
obj = Type.objects.filter(name__in =['Accionista','Presidente']).exclude(id=1)
#VER EL QUERY QIE EJECUTA LA SENTENCIA
obj = Type.objects.filter(name__iregex ='Aux').query
#print(obj)

#EMPLEADOS CON SON DEL TIPO 1
obj = Employee.objects.filter(type_id=1)
#ITERAR
for i in Type.objects.filter():
    print(i.name)