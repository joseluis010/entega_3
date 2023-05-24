from django.db import models

class Post(models.Model):
    título = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self) -> str:
        return self.título

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
    