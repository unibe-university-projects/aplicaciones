from django.db import models

from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    # Additional fields
    email = models.EmailField(max_length=254)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    ocupacion = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50)
    altura = models.FloatField()
    peso = models.FloatField()
    color_ojos = models.CharField(max_length=50)
    color_cabello = models.CharField(max_length=50)
    nivel_educativo = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    hobbies = models.TextField()
    redes_sociales = models.TextField()
    idiomas = models.TextField()
    deportes = models.TextField()
    habilidades = models.TextField()
    alergias = models.TextField()
    medicamentos = models.TextField()
    enfermedades_cronicas = models.TextField()
    emergencia_contacto_nombre = models.CharField(max_length=100)
    emergencia_contacto_telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre
