from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib import admin


class Usuario(models.Model):
    Nombre_Completo = models.CharField(max_length=200)
    Dpi = models.CharField(max_length=13)

    
    def __unicode__(self):
        return self.Nombre_Completo
    
    def __str__(self):
        return self.Nombre_Completo
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
    
class Libros(models.Model):
    user = models.ForeignKey('auth.User')
    ISBN = models.CharField(max_length = 13)
    titulo = models.CharField(max_length=200)
    #imagen = models.ImageField(upload_to=upload_location,null=True, blank=True,width_field="width_field",height_field="height_field")
    #height_field = models.IntegerField(default=0)
    #width_field = models.IntegerField(default=0)
    Autor =models.CharField(max_length=200)
    Editorial = models.CharField(max_length=200)
    Pais = models.CharField(max_length=200)
    Anio = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    Usuar = models.ManyToManyField(Usuario, through='Prestamo')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __unicode__(self):
        return self.titulo
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})




class Prestamo(models.Model):
    User = models.ForeignKey(Usuario,related_name ='usuario', on_delete=models.CASCADE)
    Libro = models.ForeignKey(Libros,related_name ='libros',on_delete=models.CASCADE)
    Fecha_prestamo = models.DateTimeField(auto_now=False, auto_now_add=True)
    Fecha_devolucion = models.DateTimeField(auto_now=False, auto_now_add=False)
    Fecha_devolucionReal = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __unicode__(self):
        return self.User
    
    def __str__(self):
        return self.Libro
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
    
class PrestamoInLine(admin.TabularInline):

    model = Prestamo

    extra = 1


class LibroAdmin(admin.ModelAdmin):

    inlines = (PrestamoInLine,)


class UsuarioAdmin (admin.ModelAdmin):

    inlines = (PrestamoInLine,)