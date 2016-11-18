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
    
    
    
def __init__ (self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.       

        self.fields["Usuar"].widget = forms.widgets.CheckboxSelectMultiple()

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["Usuar"].queryset = Usuario.objects.all()