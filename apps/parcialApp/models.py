from __future__ import unicode_literals
from django.db import models
#imports new user

#create your models here

class empleado(models.Model):
	nombre = models.CharField(max_length = 45)
	dpi = models.CharField(max_length = 25)
	telefono = models.CharField(max_length = 15)
	fecha = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s' % (self.nombre)

class cliente(models.Model):
	nombre = models.CharField(max_length = 45)
	dpi = models.CharField(max_length = 15)
	fecha = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s' % (self.nombre)

class pedido(models.Model):
	empleado_pedido = models.ForeignKey(empleado, null = True)
	cliente_pedido = models.ForeignKey(cliente)
	nit = models.CharField(max_length = 10)
	nombre_de_negocio = models.CharField(max_length = 45)
	cantidad = models.IntegerField()
	tamano_choices = (
		('0', 'cuarto de oficio'),
		('1', 'media carta'),
		('2', 'carta'),
		('3', 'oficio'),
		)
	tamano = models.CharField(
	max_length=1,
	choices = tamano_choices,
	default = '0',
	)
	
	tipo_papel_choices = (
		('0', 'normal'),
		('1', 'sensibilizado'),
		)
	tipo_papel = models.CharField(
	max_length=1,
	choices = tipo_papel_choices,
	default = '0',
	)
	precio_pedido = models.IntegerField()
	estado_pedido = models.BooleanField(default=False)
	fecha_pedido = models.DateTimeField(auto_now_add = True)
	fecha_entrega = models.DateTimeField()

	def __str__(self):
		return '%s %s' % (self.nit,self.nombre_de_negocio)

	def get_tipo_papel(self):
		return self.tipo_papel

	def get_tamano(self):
		return self.tamano

	def get_estado(self):
		return self.estado_pedido