"""myPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from .views import vistaPrincipal,vistaEmpleado,vistaCliente,vistaPedido,LoginView,listaEmpleado,listaCliente,listaPedido,CrearUsuarioView
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required, permission_required
from .views import editar_cliente,eliminar_cliente,editar_empleado,eliminar_empleado,editar_pedido,eliminar_pedido

urlpatterns = [
	url(r'^$', vistaPrincipal.as_view()),
	url(r'^principal$', vistaPrincipal.as_view(), name = 'principal'),
    url(r'^login$', LoginView.as_view(), name = 'login'),
    
	url(r'^empleado$', login_required(vistaEmpleado.as_view()), name = 'empleado'),
    url(r'^listaEmpleado$', login_required(listaEmpleado.as_view()), name = 'listaEmpleado'),
    url(r'^editar_empleado/(?P<pk>\d+)/', editar_empleado.as_view(), name = 'editar_empleado'),
    url(r'^eliminar_empleado/(?P<pk>\d+)/$', eliminar_empleado.as_view(), name = 'eliminar_empleado'),

    url(r'^cliente$', login_required(vistaCliente.as_view()), name = 'cliente'),
    url(r'^listaCliente$', login_required(listaCliente.as_view()), name = 'listaCliente'),
    url(r'^editar_cliente/(?P<pk>\d+)/', editar_cliente.as_view(), name = 'editar_cliente'),
    url(r'^eliminar_cliente/(?P<pk>\d+)/$', eliminar_cliente.as_view(), name = 'eliminar_cliente'),

    url(r'^pedido$', login_required(vistaPedido.as_view()), name = 'pedido'),
    url(r'^listaPedido$', login_required(listaPedido.as_view()), name = 'listaPedido'),
    url(r'^editar_pedido/(?P<pk>\d+)/', editar_pedido.as_view(), name = 'editar_pedido'),
    url(r'^eliminar_pedido/(?P<pk>\d+)/$', eliminar_pedido.as_view(), name = 'eliminar_pedido'),

    #url(r'^accounts/login/$', login, name = 'login'),
    url(r'^logout/$', logout, {'template_name': 'principal.html'}, name = 'logout'),
]

#13,8
#16,7
#12,15