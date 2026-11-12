from django.db import models

class Noticia (models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    fecha = models.DateField()
    lugar= models.CharField(max_length=100, verbose_name="Lugar")
    descripsion= models.TextField()
    imagen= models.ImageField(upload_to='noticias/', verbose_name="Imagen")


    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo