from django.db import models
from django.utils import timezone

class Producto(models.Model):
    Nombre = models.CharField(max_length=200)
    Creado = models.DateTimeField(
            default=timezone.now)
    Fecha_de_Compra = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.Fecha_de_Compra = timezone.now()
        self.save()

    def __str__(self):
        return self.title
