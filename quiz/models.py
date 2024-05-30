from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    ficha = models.IntegerField()

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


    def __str__(self):
        return self.nombre