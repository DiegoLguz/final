from django import forms
from .models import Libros
from .models import Usuario
from .models import Prestamo
from django.forms import ModelForm

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = [
            "ISBN",
            "titulo",
            "Autor",
            "Editorial",
            "Pais",
            "Anio",
        ]  
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "Nombre_Completo",
            "Dpi",
        ]
        
class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['User', 'Libro', 'Fecha_devolucion', 'Fecha_devolucionReal']
    
    
    
    