from django.conf.urls import include,url
from exfinal import views as post_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_views.lista, name ="lista"),
    url(r'^nuevo/', post_views.nuevo, name ="nuevo"),
    url(r'^usuario/', post_views.nuevoU, name ="nuevoU"),
    url(r'^prestamo/', post_views.prestamo, name ="prestamo"),
]
