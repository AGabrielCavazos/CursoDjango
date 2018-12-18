from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100,unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace",max_length=200,null=True,blank = True)
    created = models.DateTimeField(auto_now_add="true", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now="true", verbose_name="ultima modificacion")

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]
    
    def __str__(self):
        return self.name