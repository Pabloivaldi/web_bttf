from django.contrib import admin

from .models import Project  # importamos la clase
# Register your models here.    registramos

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    


admin.site.register(Project, ProjectAdmin)
