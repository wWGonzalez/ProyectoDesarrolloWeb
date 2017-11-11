from django.conf.urls import url,include
from .views import RegistroUsuario
from django.contrib.auth.decorators import login_required, permission_required
#from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^Registro$', login_required(RegistroUsuario.as_view()),name='Registro'),
]