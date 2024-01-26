from django.urls import path
from finalApp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView




urlpatterns = [

    path("", index, name = "index"),

    path("registro-usuario/", registroUsuario, name = "registroUsuario"),
    path("registro-publicacion/", registroPublicacion, name = "registroPublicacion"),
    path("registro-comentario/", registroComentario, name = "registroComentario"),
    
    path("listar-usuarios/", listarUsuarios, name = "listarUsuarios"),
    path("listar-publicaciones/", listarPublicaciones, name = "listarPublicaciones"),
    path("listar-comentarios/", listarComentarios, name = "listarComentarios"),

    path("eliminar-usuario/<usuario>/", eliminarUsuario, name = "eliminarUsuario"),
    path("eliminar-publicacion/<publicacion>/", eliminarPublicacion, name = "eliminarPublicacion"),
    path("eliminar-comentarios/<comentario>/", eliminarComentario, name = "eliminarComentario"),

    path("editar-publicacion/<publicacion_nombre>/", editarPublicacion , name = "editarPublicacion"),

    path("login/", login_request, name = "login"),
    path("registrar/", registrar, name = "registrar"),
    path("logout/", LogoutView.as_view(template_name= "logout.html"), name = "logout"),
]

urlpatterns += staticfiles_urlpatterns()
