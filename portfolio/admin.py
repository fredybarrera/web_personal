from django.contrib import admin
from .models import Project

# Register your models here.

# Permite redefinir configuraciones en el modelo, en este caso de definen los campos "created" y "updated" solo de lectura.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)