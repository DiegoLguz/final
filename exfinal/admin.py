from django.contrib import admin
from exfinal.models import Libros
from exfinal.models import Usuario
from exfinal.models import Prestamo


class LibroModelAdmin(admin.ModelAdmin):
    list_display= ["user","ISBN","titulo","Autor","Editorial","Pais","Anio","created_date"]
    list_display_links = ["ISBN"]
    list_filter = ["titulo","created_date"]
    list_editable = ["titulo","Autor","Editorial"]
    search_fields = ["titulo"]
    class Meta:
        model = Libros
        
class UsuarioModelAdmin(admin.ModelAdmin):
    list_display= ["Nombre_Completo","Dpi"]
    list_display_links = ["Dpi"]
    list_filter = ["Dpi"]
    list_editable = ["Nombre_Completo"]
    search_fields = ["Dpi"]
    class Meta:
        model = Usuario

class PrestamoModelAdmin(admin.ModelAdmin):
    list_display= ["User","Libro","Fecha_prestamo","Fecha_devolucion","Fecha_devolucionReal"]
    list_display_links = ["Fecha_prestamo"]
    list_filter = ["Fecha_prestamo"]
    list_editable = ["Fecha_devolucionReal"]
    search_fields = ["Fecha_devolucion"]
    class Meta:
        model = Prestamo
        
admin.site.register(Prestamo, PrestamoModelAdmin)
admin.site.register(Libros,LibroModelAdmin)
admin.site.register(Usuario,UsuarioModelAdmin)

