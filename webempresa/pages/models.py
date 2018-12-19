from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add="true", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now="true", verbose_name="ultima modificacion")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["title"]
    
    def __str__(self):
        return self.title