from django.urls import path
from ProyectowebApp import views
from django.contrib.auth.views import LoginView

#from django.config import settings
#from django.config.urls.static import static
 

urlpatterns = [
    path('',views.index, name="inicio"),
    path('principalencargados',views.principalencargados, name="principal"),
    path('prueba',views.prueba, name="prueba"),
    path('inicioSesion', views.inicioSesion, name="inicioSesion"),
    path('perfil', views.perfil, name="perfil"),
    path('login', views.login, name="login"),
    path('registro', views.registro, name="registro"), 
    path('logout', views.logout, name="logout"),
    path('chat', views.chat, name="chat"),
    path('mensajeEnviado', views.mensajeEnviado, name="mensajeEnviado"),
    path('chatencargados',views.chatencargados, name="chatencargados"),  
    path('mensajerespuesta', views.mensajerespuesta, name="mensajerespuesta"),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)