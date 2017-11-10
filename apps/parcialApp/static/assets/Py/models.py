# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class empleado(models.Model):
	nombre = models.CharField(max_length = 45)
	telefono = models.CharField(max_length = 15)
	contrasena = models.CharField(max_length = 50)
	fecha = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s %s' % (self.nombre,self.creacion)

class cliente(models.Model):
	nombre = models.CharField(max_length = 45)
	telefono = models.CharField(max_length = 15)
	contrasena = models.CharField(max_length = 50)
	fecha = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s %s' % (self.nombre,self.creacion)

class pedidos(models.Model):
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
	tamano = models.CharField(
	max_length=1,
	choices = tipo_papel_choices,
	default = '0',
	)

	precio = models.IntegerField()
	fecha = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s %s' % (self.nombre,self.creacion)