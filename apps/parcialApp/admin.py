from django.contrib import admin
from .models import empleado,cliente,pedido
# Register your models here.
admin.site.register(empleado)
admin.site.register(cliente)
admin.site.register(pedido)