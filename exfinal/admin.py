from django.contrib import admin
from exfinal.models import Libros, LibroAdmin
from exfinal.models import Usuario, UsuarioAdmin
        
admin.site.register(Libros,LibroAdmin)
admin.site.register(Usuario,UsuarioAdmin)

