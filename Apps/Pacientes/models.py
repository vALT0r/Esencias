from django.db import models

# Create your models here.

class Paciente(models.Model):
    Apellido = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)
    DNI = models.CharField(max_length=12, blank=True)
    FechaNacimiento = models.DateField(blank=True)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='F', blank=True)
    Direccion = models.CharField(max_length=60, blank=True)
    Telefono = models.CharField(max_length=20, blank=True)
    Localidad = models.CharField(max_length=30, blank=True)
    Email = models.EmailField(blank=True)
    SINO = (('N', 'No'), ('S', 'Si'))
    Psicologo = models.CharField(max_length=1, choices=SINO, default='N', blank=True)

    def nombrecompleto(self):
        return "{0:05d} - {1}, {2}".format(self.id, self.Apellido, self.Nombre)

    def __str__(self):
        return self.nombrecompleto()


class Consulta(models.Model):
    Paciente = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)
    FechaHora = models.DateTimeField(auto_now_add=True)
    Observaciones = models.CharField(max_length=2000, blank=True)
    Receta = models.CharField(max_length=500, blank=True)

    def __str__(self):
        cadena = "{0} - {1} - {2}"
        fecha = self.FechaHora.strftime("%d/%m/%y")
        return cadena.format(self.Paciente, fecha, self.Receta)
