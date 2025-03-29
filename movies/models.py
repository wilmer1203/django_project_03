from django.db import models

# Create your models here.

class Pelicula(models.Model):
    GENEROS = [
        ('ACC', 'Acción'),
        ('DRM', 'Drama'),
        ('CMD', 'Comedia'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    año = models.PositiveIntegerField()
    genero = models.CharField(max_length=3, choices=GENEROS)
    director = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.año})"