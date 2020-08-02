from django.db import models

GENERO = [('H','Hombre'),('M','Mujer')]
 
class Profesor(models.Model):
    Nombre_y_apellido = models.CharField(max_length=100)
    Asignatura = models.CharField(max_length=60)
    tiempo_exp = models.IntegerField()
    trayectoria_resumen = models.TextField(blank=True)
    sexo = models.CharField(choices=GENERO, max_length=1)

class Estudiante(models.Model):
    Nombre_y_apellido = models.CharField(max_length=100)
    Carrera = models.CharField(max_length=60)
    Promedio = models.DecimalField(decimal_places=2, max_digits=4)
    Semestres_cursados = models.IntegerField()
    correo = models.EmailField()
    sexo = models.CharField(choices=GENERO, max_length=1)