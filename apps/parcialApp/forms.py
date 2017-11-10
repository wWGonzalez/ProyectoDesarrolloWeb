from django import forms
#from django import forms.ModelForm
from .models import empleado,cliente,pedido

class empleadoForm(forms.ModelForm):
	class Meta:
		model = empleado
		fields = '__all__'

class clienteForm(forms.ModelForm):
	class Meta:
		model = cliente
		fields = '__all__'

class pedidoForm(forms.ModelForm):
	class Meta:
		model = pedido
		fields = '__all__'