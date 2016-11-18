from django.shortcuts import render
from .models import Libros
from .models import Usuario
from .models import Prestamo
from .forms import LibrosForm
from .forms import UsuarioForm
from .forms import PrestamoForm
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse

def nuevo(request):
    form = LibrosForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('login')) 
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)


def nuevoU(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista')) 
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)

def prestamo(request):
    form = PrestamoForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        libro = LIbros.objects.create(Usuario =formulario.cleaned_data['User'], Libro = formulario.cleaned_data['Libro'])
        for libro_id in request.POST.getlist('Libro'):
            prestamo = Prestamo(libro_id=libro_id, usuario_id=usuario.id)
            prestamo.save()
        instance.user = request.user
        instance.save()
    else:
        form2 = LibrosForm()

    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)



def lista(request):
    queryset = Libros.objects.all().order_by("-created_date")
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
        }
    else:
        context = {
            "title": "Inicie sesion para ver la lista de articulos"
        }
    return render(request,"index.html",context)

