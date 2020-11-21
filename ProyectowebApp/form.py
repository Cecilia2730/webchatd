from django import forms

from .models import Usuarios
from .models import Mensajes

class UsuarioForm(forms.ModelForm):

	class Meta:
		model=Usuarios

		fields=[
			'id_departamento',
			'NombreUsuario',
			'Password',
			'Telefono',
			
		]

class Mensajeform(forms.ModelForm):
	class Meta:
		model=Mensajes

		fields=[
			'id_departamento',
			'Mensaje',
			'Status_recibido',
			'Status_respuesta',
			'Ip',]
					
