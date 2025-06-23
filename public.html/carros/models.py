from django.db import models

# Create your models here.

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    quilometragem = models.PositiveIntegerField()
    numero_portas = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    combustivel = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='carros/')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
