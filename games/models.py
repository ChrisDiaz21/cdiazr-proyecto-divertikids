from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=80, verbose_name="Título")
    price = models.IntegerField(verbose_name="Precio")
    imagen = models.ImageField(upload_to="games", verbose_name="Imagen", null=True)
    description = models.TextField(verbose_name="Descripción")

    # Edad permitida en un rango
    age_min = models.IntegerField(verbose_name="Edad mínima permitida", null=True)
    age_max = models.IntegerField(verbose_name="Edad máxima permitida", null=True)

    # Dimensiones de los juegos: ancho y largo
    width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ancho (m)", null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Largo (m)", null=True)

    stock = models.IntegerField(verbose_name="Cantidad")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.title
