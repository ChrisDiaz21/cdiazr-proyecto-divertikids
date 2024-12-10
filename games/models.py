from django.db import models

# Create your models here.

class Products(models.Model):

    title=models.CharField(max_length=80,verbose_name="Titulo")
    price=models.IntegerField(verbose_name="Precio")
    imagen=models.ImageField(upload_to="games",verbose_name="imagen", null=True )
    description=models.TextField(verbose_name="Descripcion")
    age=models.TextField(verbose_name="Edad permitida")
    stock=models.IntegerField(verbose_name="Cantidad")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.title
