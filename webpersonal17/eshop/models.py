from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=20, verbose_name='Titulo')
    descripcion= models.TextField(verbose_name='Descripción')
    image=models.ImageField(verbose_name='Imagen', upload_to="projects")
    link=models.URLField(verbose_name='enlace', null=True, blank= True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    
    
    def __str__(self) -> str:
        return self.title
    
    
    #subclase para cambiar algunos nombres:
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'   
        ordering= ['-created'] #este ATRIBUTO esta diciendo que el campo created (linea 9) tenga un orden desendente (que el ultimo aparezca primero), porque tiene un menos (-), sin ese menos el orden es ascendente.
  