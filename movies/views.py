from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView
from movies.models import Pelicula

class ListaPeliculas(ListView):
    model = Pelicula
    template_name = 'lista_peliculas.html'
    context_object_name = 'peliculas'
    ordering = ['-fecha_creacion']
    paginate_by = 10 
    


def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula})

    
class MovieDetailView(DetailView):
    model = Pelicula
    template_name = 'detalle_pelicula.html'
    context_object_name = 'pelicula'
   
