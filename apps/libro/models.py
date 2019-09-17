from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de Publicación', blank=False, null=False)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo
