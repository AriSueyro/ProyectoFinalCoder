from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
class PublicacionFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    detalle = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}))
    imagen = forms.ImageField()

class ComentarioFormulario(forms.Form):
    asunto = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    texto = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    