from django.contrib.auth.models import User
from django.db import models

class Maullido(models.Model):
    """Modelo para los maullidos"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=140)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido[:50]
