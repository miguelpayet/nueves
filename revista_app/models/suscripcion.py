from django.db import models


class Suscripcion(models.Model):
    idsuscripcion = models.AutoField(primary_key=True)
    email = models.CharField(max_length=256, blank=False, null=False)
    creacion = models.DateTimeField()

    class Meta:
        db_table = 'suscripcion'
        verbose_name = "Suscripción"
        verbose_name_plural = "Suscripciones"
