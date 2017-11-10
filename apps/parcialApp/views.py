#para el logueo de los usuarios
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView
#estas tres lineas
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .models import empleado,cliente,pedido
from .forms import empleadoForm,clienteForm,pedidoForm
# Create your views here.

class vistaPrincipal(TemplateView):
	template_name = 'principal.html'

#estudiante
class vistaEmpleado(CreateView):
	template_name = 'empleado.html'
	form_class = empleadoForm
	success_url = reverse_lazy('parcial1:empleado')

class listaEmpleado(ListView):
	template_name = 'listaEmpleado.html'
	model = empleado

	def get_queryset(self):
		return empleado.objects.all()

class editar_empleado(UpdateView):
	template_name = 'empleado.html'
	model = empleado
	form_class = empleadoForm
	success_url = reverse_lazy('parcial1:listaEmpleado')

class eliminar_empleado(DeleteView):
	template_name = 'eliminar.html'
	model = empleado
	success_url = reverse_lazy('parcial1:listaEmpleado')
#end empleado


#estudiante
class vistaCliente(CreateView):
	template_name = 'cliente.html'
	form_class = clienteForm
	success_url = reverse_lazy('parcial1:cliente')

class listaCliente(ListView):
	template_name = 'listaCliente.html'
	model = cliente

	def get_queryset(self):
		return cliente.objects.all()

class editar_cliente(UpdateView):
	template_name = 'cliente.html'
	model = cliente
	form_class = clienteForm
	success_url = reverse_lazy('parcial1:listaCliente')

class eliminar_cliente(DeleteView):
	template_name = 'eliminar.html'
	model = cliente
	success_url = reverse_lazy('parcial1:listaCliente')
#end cliente


#pedido
class vistaPedido(CreateView):
	template_name = 'pedido.html'
	form_class = pedidoForm
	success_url = reverse_lazy('parcial1:pedido')

class listaPedido(ListView):
	template_name = 'listaPedido.html'
	model = pedido

	def get_queryset(self):
		return pedido.objects.all()

class editar_pedido(UpdateView):
	template_name = 'pedido.html'
	model = pedido
	form_class = pedidoForm
	success_url = reverse_lazy('parcial1:listaPedido')

class eliminar_pedido(DeleteView):
	template_name = 'eliminar.html'
	model = pedido
	success_url = reverse_lazy('parcial1:listaPedido')
#end pedido





#login
class LoginView(FormView):
	template_name = 'login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('parcial1:principal')

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)


class CrearUsuarioView(CreateView):
	model = User
	template_name = 'CrearUsuario.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('parcial1:principal')