from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    ROLES_CHOIcES = [
        ('usuario_final', "Usuario Final"),
        ('productor', "Productor"),
        ('comerciante', "Comerciante"),
    ]
    
    rol = models.CharField(max_length=20, choices=ROLES_CHOIcES)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    identificacion = models.CharField(max_length=12, unique=True)
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)
    terminos = models.BooleanField(default=False)    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.get_rol_display()}"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"