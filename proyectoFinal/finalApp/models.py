from django.db import models
from datetime import datetime


class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return (f"{self.nombre}, {self.apellido}, {self.mail}, {self.edad}")
    
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    imagen = models.FileField(upload_to='static/img/', null = True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.titulo}, {self.detalle}")

class Comentario(models.Model):
    asunto = models.CharField(max_length=50)
    texto = models.TextField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.asunto}, {self.texto}, {self.fecha}")


