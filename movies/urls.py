from django.urls import path
from movies.views import ListaPeliculas , MovieDetailView, detalle_pelicula

urlpatterns = [
    path('', ListaPeliculas.as_view(), name='lista_peliculas'),
    path('movie/pelicula/<int:pelicula_id>/', detalle_pelicula, name='detalle_pelicula'),
    path('pelicula/<int:pk>/', MovieDetailView.as_view(), name='detalle_pelicula'), 
]