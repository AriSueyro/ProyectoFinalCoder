from django.urls import path
from finalApp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path("", inicio, name = "index"),
    path("registro-usuario/", registroUsuario, name = "registroUsuario"),
    path("registro-publicacion/", registroPublicacion, name = "registroPublicacion"),
    path("registro-comentario/", registroComentario, name = "registroComentario"),
    
    path("listar-usuarios/", listarUsuarios, name = "listarUsuarios"),
    path("listar-publicaciones/", listarPublicaciones, name = "listarPublicaciones"),
]

urlpatterns += staticfiles_urlpatterns()
