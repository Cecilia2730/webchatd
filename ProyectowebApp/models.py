from django.db import models

class Departamentos(models.Model):
	id_Departamento= models.AutoField(primary_key=True)
	Nombre=models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.Nombre
		return self.id_Departamento

class Usuarios(models.Model):
	id_departamento=models.ForeignKey(Departamentos, on_delete=models.CASCADE)
	idUsuario=models.AutoField(primary_key=True)
	NombreUsuario=models.CharField(max_length=50, unique=True)
	Password=models.CharField(max_length=15, unique=True)
	Telefono=models.IntegerField(unique=True)
	

	def __str__(self):
		return self.NombreUsuario
		return self.Password
		return self.Telefono
		return self.id_departamento

class Mensajes(models.Model):
	id_departamento=models.IntegerField(default=0)
	idMensaje=models.AutoField(primary_key=True)
	Mensaje=models.CharField(max_length=200, unique=True)
	Status_recibido=models.IntegerField(default=1)
	Status_respuesta=models.IntegerField(default=2)
	Ip=models.CharField(max_length=20, default=0)

	def __str__(self):
		return self.Mensaje
		return self.Ip
		return self.Status_recibido
		return self.id_departamento
		return self.Status_respuesta
		

		
		


