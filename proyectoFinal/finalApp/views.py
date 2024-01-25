from django.shortcuts import render
from django.http import HttpResponse
from finalApp.forms import *
from finalApp.models import *
from django.views.generic import UpdateView

def inicio(request):
    return render(request, "index.html")

def pinto(request):
    return render(request, "")

def aver(request):
    return render(request, "gallery.html")

def registroUsuario(request):

    if request.method == "POST":
        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = Usuario(nombre = datos.get("nombre"), apellido = datos.get("apellido"), edad = datos.get("edad"), mail = datos.get("mail"))
            usuario.save()

            return render(request, "index.html")
        
    else:
        formulario = UsuarioFormulario()

    return render(request, "formUsuario.html", {'formulario': formulario})

def listarUsuarios(request):
    usuarios = Usuario.objects.all()

    contexto = {"usuarios": usuarios}

    return render(request, "listadoUsuario.html", contexto)

def eliminarUsuario(request, usuario):
    usuario = Usuario.objects.get(mail = usuario)
    usuario.delete()

    usuarios = Usuario.objects.all()

    contexto = {"usuarios": usuarios}

    return render(request, "listadoUsuario.html", contexto)



def registroPublicacion(request):

    if request.method == "POST":
        formulario = PublicacionFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            publicacion = Publicacion(titulo = datos.get("titulo"), detalle = datos.get("detalle"), imagen = datos.get("imagen"))
            publicacion.save()

            return render(request, "index.html")

    else:
        formulario = PublicacionFormulario()

    return render(request, "formPublicacion.html", {'formulario': formulario})

def listarPublicaciones(request):
    publicaciones = Publicacion.objects.all()

    contexto = {'publicaciones': publicaciones}

    return render(request, "listadoPublicaciones.html", contexto)

class editarPublicaciones(UpdateView):
    model = Publicacion
    fields = ['titulo', 'detalle', 'imagen']
    template_name = "formPublicacion.html"
    success_url = "listarPublicaciones.html"

def eliminarPublicacion(request, publicacion):
    publicacion = Publicacion.objects.get(titulo = publicacion)
    publicacion.delete()

    publicaciones = Publicacion.objects.all()

    contexto = {"publicaciones": publicaciones}

    return render(request, "listadoPublicaciones.html", contexto)


def registroComentario(request):

    if request.method == "POST":
        formulario = ComentarioFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            comentario = Comentario(asunto = datos.get("asunto"), texto = datos.get("texto"), fecha = datos.get("fecha"))
            comentario.save()

            return render(request, "index.html")  

    else:
        formulario = ComentarioFormulario()

    return render(request, "formComentario.html", {'formulario' : formulario})    


def listarComentarios(request):
    comentarios = Comentario.objects.all()

    contexto = {'comentarios': comentarios}

    return render(request, "listadoComentarios.html", contexto)

def eliminarComentario(request, comentario):
    comentario = Comentario.objects.get(asunto = comentario)
    comentario.delete()

    comentarios = Comentario.objects.all()

    contexto = {"comentarios": comentarios}

    return render(request, "listadoComentarios.html", contexto)




