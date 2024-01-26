from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
class PublicacionFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    detalle = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}))
    imagen = forms.ImageField()

class PublicacionEditarFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    detalle = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}))  

class ComentarioFormulario(forms.Form):
    asunto = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    texto = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'last_name', 'first_name']
    

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'last_name', 'first_name']
    