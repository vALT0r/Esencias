from django import forms
from django.db import models


# Create your models here.

class Esencia(models.Model):
    Nombre = models.CharField(max_length=100)
    NombreCientifico = models.CharField(max_length=100, blank=True)
    Subtitulo = models.CharField(max_length=301, blank=True)
    Positivos = models.CharField(max_length=302, blank=True)
    Negativos = models.CharField(max_length=303, blank=True)
    Descripcion = models.TextField(max_length=10000, blank=True)
    TestIntuitivo = models.CharField(max_length=10000, blank=True)
    DescripcionCorta = models.CharField(max_length=5000, blank=True)
    Imagen = models.CharField(max_length=304, blank=True)
    OpcionesSet = (('0', 'Set 100 Flores'), ('1', 'Nuevas Flores'))
    Sets = models.CharField(max_length=1, blank=False, default='0', choices=OpcionesSet)
    Pregunta1 = models.CharField(max_length=305, blank=True)
    Pregunta2 = models.CharField(max_length=306, blank=True)
    Pregunta3 = models.CharField(max_length=307, blank=True)
    Pregunta4 = models.CharField(max_length=308, blank=True)
    Pregunta5 = models.CharField(max_length=309, blank=True)
    PlusInfo = models.CharField(max_length=10000, blank=True)
    DSAA = (('Desconocido', 'Desconocido'), ('Sedativa', 'Sedativa'), ('Activadora', 'Activadora'), ('Ambas', 'Ambas'))
    Efecto = models.CharField(max_length=12, blank=False, default='Desconocido', choices=DSAA)

    def nombresubtitulo(self):
        return "{0} - {1}".format(self.Nombre, self.Subtitulo)

    def __str__(self):
        return self.nombresubtitulo()


class Formula(models.Model):
    Nombre = models.CharField(max_length=100)
    Subtitulo = models.CharField(max_length=200, blank=True)
    Esencia = models.ManyToManyField(Esencia)
    SubFormula = models.ManyToManyField('self', blank=True, symmetrical=False)
    Subtitulo = models.CharField(max_length=301, blank=True)
    Positivos = models.CharField(max_length=302, blank=True)
    Negativos = models.CharField(max_length=303, blank=True)
    Descripcion = models.TextField(max_length=10000, blank=True)
    TestIntuitivo = models.CharField(max_length=10000, blank=True)
    DescripcionCorta = models.CharField(max_length=5000, blank=True)
    Pregunta1 = models.CharField(max_length=305, blank=True)
    Pregunta2 = models.CharField(max_length=306, blank=True)
    Pregunta3 = models.CharField(max_length=307, blank=True)
    Pregunta4 = models.CharField(max_length=308, blank=True)
    Pregunta5 = models.CharField(max_length=309, blank=True)
    SINO = (('N', 'No'), ('S', 'Si'))
    Personalizada = models.CharField(max_length=1, blank=False, default='N', choices=SINO)

    def returnformula(self):
        return "{}".format(self.Nombre)

    def __str__(self):
        return self.returnformula()


class Sintoma(models.Model):
    Sintoma = models.CharField(max_length=30)

    def returnsintoma(self):
        return "{0}".format(self.Sintoma)

    def __str__(self):
        return self.returnsintoma()


class Subsintoma(models.Model):
    Sintoma = models.ForeignKey(Sintoma, null=False, blank=False, on_delete=models.CASCADE)
    Subsintoma = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200, blank=True)
    Esencia = models.ManyToManyField(Esencia, blank=True)
    Formula = models.ManyToManyField(Formula, blank=True)

    def returnsubsintoma(self):
        return "{}".format(self.Subsintoma)

    def __str__(self):
        return self.returnsubsintoma()


class Paciente(models.Model):
    SI = (('No', 'No'), ('Si', 'Si'))
    SEXOS = (('Femenino', 'Femenino'), ('Masculino', 'Masculino'))
    SINO = (('No', 'No'), ('Si', 'Si'), ('Ultimo Año', 'Ultimo Año'), ('Mas de 1 Año', 'Mas de 1 Año'))
    DiabOps = (('No', 'No'), ('Sin Insulina', 'Sin Insulina'), ('Con Insulina', 'Con Insulina'))
    AlimOps = (('Mala', 'Mala'), ('Regular', 'Regular'), ('Buena', 'Buena'))

    Nombre = models.CharField(max_length=35, verbose_name='Nombre')
    Apellido = models.CharField(max_length=35, verbose_name='Apellido')
    FechaNacimiento = models.DateField(max_length=60, blank=True, verbose_name='Fecha de Nacimiento')
    HoraNacimiento = models.TimeField(max_length=60, blank=True, default="00:00:00", verbose_name='Hora de Nacimiento')
    LugarNacimiento = models.CharField(max_length=60, blank=True, verbose_name='Lugar de Nacimiento')
    Sexo = models.CharField(max_length=12, choices=SEXOS, default='Femenino', verbose_name='Sexo')
    Direccion = models.CharField(max_length=60, blank=True, verbose_name='Dirección')
    Localidad = models.CharField(max_length=30, blank=True, verbose_name='Localidad')
    Telefono = models.CharField(max_length=20, blank=True, verbose_name='Telefono')
    Email = models.EmailField(blank=True, verbose_name='Direccion de E-Mail')
    Profesion = models.CharField(max_length=50, blank=True, verbose_name='Profesión')
    Recomendado = models.CharField(max_length=70, blank=True, verbose_name='Recomendado por')
    Hijos = models.CharField(max_length=100, blank=True, verbose_name='Hijos')
    Hermanos = models.CharField(max_length=200, blank=True, verbose_name='Hermanos')
    Pareja = models.CharField(max_length=12, choices=SI, default='N', verbose_name='Pareja')
    ParejaTiempo = models.CharField(max_length=50, blank=True, verbose_name='Tiempo en Pareja')
    Psicologo = models.CharField(max_length=12, choices=SINO, default='N', verbose_name='Psicologo')
    Constelaciones = models.CharField(max_length=12, choices=SINO, default='N', verbose_name='Constelaciones')
    Alimentacion = models.CharField(max_length=12, choices=AlimOps, default='N', verbose_name='Alimentacion')
    Yoga = models.CharField(max_length=12, choices=SINO, default='N', verbose_name='Yoga')
    Anemia = models.CharField(max_length=12, choices=SI, default='N', verbose_name='Anemia')
    Diabetes = models.CharField(max_length=12, choices=DiabOps, default='N', verbose_name='Diabetes')
    Operaciones = models.CharField(max_length=200, blank=True, verbose_name='Operaciones')
    Medicacion = models.CharField(max_length=200, blank=True, verbose_name='Toma Alguna Medicacion?')
    EnfermedadesPasadas = models.CharField(max_length=200, blank=True, verbose_name='Enfermedades en el Pasado')
    EnfermedadesActuales = models.CharField(max_length=200, blank=True, verbose_name='Enfermedades actuales')
    AntecFamilMental = models.CharField(max_length=200, blank=True,
                                        verbose_name='Antecedentes de Salud Mental en Familiares')
    Abortos = models.CharField(max_length=200, blank=True, verbose_name='Abortos')
    OtrosSistemas = models.CharField(max_length=12, choices=SI, default='N', verbose_name='Otros Sistemas')
    DetalleSistemas = models.CharField(max_length=500, blank=True, verbose_name='¿Que sistemas?')
    MotivoVisita = models.CharField(max_length=1000, blank=True, verbose_name='Motivo de la visita')
    Observaciones = models.CharField(max_length=1000, blank=True, verbose_name='Observaciones')
    FechaAlta = models.DateTimeField(auto_now_add=True)

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


# class Test(models.Model):
#     Esencia1 = models.ForeignKey(Esencia, null=False, blank=False, on_delete=models.CASCADE)
#     Esencia2 = models.ForeignKey(Esencia, null=False, blank=False, on_delete=models.CASCADE)
#     Esencia3 = models.ForeignKey(Esencia, null=False, blank=False, on_delete=models.CASCADE)
#     Esencia4 = models.ForeignKey(Esencia, null=False, blank=False, on_delete=models.CASCADE)
#     Tipo = models.CharField(max_length=1, verbose_name='Tipo')