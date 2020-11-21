from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import logout as do_logout
from django.contrib import auth
from django.http import request
from django.contrib.auth import login as do_login
from .models import Departamentos
from .models import Usuarios
from .models import Mensajes
from .form import UsuarioForm
import MySQLdb


def index(request):
	return render(request, "ProyectowebApp/index.html")

def prueba(request):
	return render(request, "ProyectowebApp/prueba.html")

def principalencargados(request):
	return render(request, "ProyectowebApp/sesion.html")

def inicioSesion(request):
	return render(request,"ProyectowebApp/cuenta.html")

def perfil(request):
	dire=Mensajes.objects.filter(Status_recibido=1)
	contex={'address':dire}
	return render(request,"ProyectowebApp/perfil.html",contex)
		 
def registro(request):
	#form=UsuarioForm()
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		# Si el formulario es válido...
		if form.is_valid():
			form.save()
		return render(request, "ProyectowebApp/sesion.html")
	else:
		form=UsuarioForm()	
	return render(request, "ProyectowebApp/registro.html", {'form': form})

def login(request):
	if request.method=="POST":
		u=request.POST['usuario']
		p=request.POST['password']
		logue=Usuarios.objects.filter(NombreUsuario=u, Password=p)
		if logue!="":
			return redirect('perfil')
		else:
			return redirect('principalencargados')
	return redirect('principalencargados')
	
		
def logout(request):
	do_logout(request)
	return render(request, "ProyectowebApp/sesion.html")


def chat(request):
	men=Mensajes.objects.filter(Status_respuesta=2)
	contex={'mensa':men}
	return render(request, "ProyectowebApp/chat.html",contex)



def mensajeEnviado(request):
	if request.method=='POST':
		messaje=request.POST["duda"]
		ipe=request.POST["direccion"]
		men=messaje.split(" ")
		for i in men:
			if i=="hola" or i=="examen" or i=="admision" or i=="recursos" or i=="credencial": 
				mensaje=Mensajes(Mensaje=messaje, Status_recibido=1, id_departamento=1, Ip=ipe, Status_respuesta=0)
				mensaje.save()
				return render(request,"ProyectowebApp/chat.html")
			elif i=="vinculacion" or i=="empresa" or i=="estancia" or i=="servicio" or i=="social": 
				mensaje=Mensajes(Mensaje=messaje, Status_recibido=1, id_departamento=2, Ip=ipe, Status_respuesta=0)
				mensaje.save()
				return render(request,"ProyectowebApp/chat.html")
			elif i=="vacante" or i=="plaza" or i=="puesto" or i=="maestro" or i=="maestra": 
				mensaje=Mensajes(Mensaje=messaje, Status_recibido=1, id_departamento=3, Ip=ipe, Status_respuesta=0)
				mensaje.save()
				return render(request,"ProyectowebApp/chat.html")
			else:
				mensaje=Mensajes(Mensaje=messaje, Status_recibido=1, id_departamento=1, Ip=ipe, Status_respuesta=0)
				mensaje.save()
				return render(request,"ProyectowebApp/chat.html")
	else:
		return render(request,"ProyectowebApp/chat.html")

def chatencargados(request):
	duda=Mensajes.objects.filter(Status_recibido=1)
	contexto={'dudas':duda}
	return render(request, "ProyectowebApp/chatEncargados.html", contexto)
	
def mensajerespuesta(request):	
	if request.method=='POST':
		messaje=request.POST['respuesta']
		ipeu=request.POST['ipeusua']
		mensaje=Mensajes(Mensaje=messaje, Status_recibido=0, Ip=ipeu, Status_respuesta=2)
		mensaje.save()
		return render(request, "ProyectowebApp/chatEncargados.html")
	return render(request, "ProyectowebApp/chatEncargados.html")

#SELECT Mensaje from proyectowebapp_mensajes INNER JOIN proyectowebapp_usuarios on proyectowebapp_mensajes.id_departamento=proyectowebapp_usuarios.id_departamento_id where idUsuario=1
