from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Alfajor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen' ,null=True)
    descripcion = models.TextField(verbose_name="Descripcion",null=True)

def __str__(self):
    return f'Nombre: {self.nombre} - Imagen:{self.imagen}- Descripcion:{self.descripcion}'

def delete(self, using=None, keep_parents=False):
    self.imagen.storage.delete(self.imagen.name)
    super(Alfajor).delete()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)



# Create your models here.
