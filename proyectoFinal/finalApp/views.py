from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from finalApp.forms import *
from finalApp.models import *
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html')


def registrar(request):
    if request.method == "POST":
        formulario = UserRegisterForma(request.POST)
        
        if formulario.is_valid():

            username = formulario.cleaned_data["username"]

            formulario.save()

            return render(request, "index.html", {"mensaje": f"El Username {username} fue dado de alta"})

    formulario = UserRegisterForma()

    return render(request, "registrar.html", {"formulario": formulario})


def login_request(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
      
        if formulario.is_valid():
            datos = formulario.cleaned_data

            username = datos["username"]
            password = datos["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)    

                return render(request, "index.html", {"mensaje": f"Bienvenido {username}"})
            else:
                return render(request, "index.html", {"mensaje": f"El usuario o la contraseña estan errados"})
        else:

            return render(request, "index.html", {"mensaje": f"Datos invalidos"})
    
    formulario = AuthenticationForm()
    
    return render(request, "formulario.html", {"formulario": formulario})

def logou(request):
    pass

    
    formulario = AuthenticationForm()

    return render(request, "login.html", {'formulario': formulario})



def registroUsuario(request):

    if request.method == "POST":
        formulario = UserRegistrationForm(request.POST)

        if formulario.is_valid():
           # datos = formulario.cleaned_data
           # usuario = Usuario(nombre = datos.get("nombre"), apellido = datos.get("apellido"), edad = datos.get("edad"), mail = datos.get("mail"))
            #usuario.save()
            username = formulario.cleaned_data.get("username")
            formulario.save()

            return render(request, "index.html", {"mensaje": f"Se dio de alta el ususario {username}"})
        
    else:
        formulario = UserRegistrationForm()

    return render(request, "formUsuario.html", {'formulario': formulario})

def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion.get('email')
            usuario.password1 = informacion.get('password1')
            usuario.password2 = informacion.get('password2')
            usuario.last_name = informacion.get('last_name')
            usuario.first_name = informacion.get('first_name')

            usuario.save()

            return render(request, "index.html")



    else:

        formulario = UserEditForm(initial = {'email': usuario.email})

        return render(request, "editarPerfil.html", {'formulario': formulario, 'usuario': usuario})

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

def editarPublicacion(request, publicacion_nombre):

    publicacion = get_object_or_404(Publicacion, titulo=publicacion_nombre)

    if request.method == 'POST':
        formulario = PublicacionFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            datos = formulario.cleaned_data

            publicacion.titulo = datos["titulo"]
            publicacion.detalle = datos["detalle"]
            publicacion.imagen = datos["imagen"]
            

            publicacion.save()

            return render(request, "index.html")
        
    formulario = PublicacionFormulario(initial= {"titulo": publicacion.titulo, "detalle" : publicacion.detalle, "imagen" : publicacion.imagen})
    contexto = {'formulario': formulario, 'publicacion_nombre': publicacion_nombre, 'publicacion_detalle': publicacion.detalle, 'publicacion_imagen': publicacion.imagen}
    return render(request, "editarPublicacion.html", contexto)


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




