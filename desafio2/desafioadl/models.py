from django.db import models

# Create your models here.

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)  # Campo id como primary key autonumérico
    descripcion = models.TextField(default="")  # Campo descripción como TextField con valor por defecto
    eliminada = models.BooleanField(default=False)  # Campo eliminada como BooleanField con valor por defecto

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)  # Campo id como primary key autonumérico
    descripcion = models.TextField(default="")  # Campo descripción como TextField con valor por defecto
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)  # Relación con Tarea
    eliminada = models.BooleanField(default=False)  # Campo eliminada como BooleanField con valor por defecto

    def __str__(self):
        return self.descripcion



