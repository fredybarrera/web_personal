from django.db import models

# Create your models here.
class Project(models.Model):
    # Campo de caracteres (varchar)
    title = models.CharField(max_length=200, verbose_name="Título")
    # Campo de texto
    description = models.TextField(verbose_name="Descripción")
    # Campo de imagen
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    # Campo de tipo url, permite valores nulos
    link = models.URLField(verbose_name="Link", null=True, blank=True)
    # Campo de fecha y hora (timestamp). Se ejecuta cuando se guarda un registro
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # Campo de fecha y hora (timestamp). Se ejecuta cuando se actualiza in registro
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización") 

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created'] # Se ordena por el campo "created" del mas nuevo al mas antiguo.

    # Permite definir el nombre que se muestra en el panel de adminitración.
    def __str__(self):
        return self.title
