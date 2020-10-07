from django.db import models
from django.utils.translation import gettext as _
from modeltranslation.admin import TranslationAdmin

# Create your models here.
class Actividad(models.Model):
    DIAS = (
        ('Monday', _("Lunes")),
        ('Tuesday', _("Martes")),
        ('Wednesday', _("Miercoles")),
        ('Thursday', _("Jueves")),
        ('Friday', _("Viernes")),
        ('Saturday', _("Sabado")),
        ('Sunday', _("Domingo")),
    )
    dia = models.CharField(max_length=100, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField(blank=True, null=True, editable=False)
    lugar = models.ForeignKey('Lugar', on_delete=models.DO_NOTHING, )
    actividad = models.TextField(max_length=100, default='')





    def __str__(self):
        return self.actividad

class Lugar(models.Model):
    codigo = models.CharField(max_length=10, blank=True, null=True, editable=False)
    nombre = models.CharField(max_length=100)
    isla = models.ForeignKey('Isla',on_delete=models.CASCADE)
    def __str__(self):
        return "Isla: %s - Lugar: %s" %(self.isla, self.nombre)

class Isla(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


