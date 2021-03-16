from django.db import models

from . import Contenido


class Narracion(Contenido):
    biografia = models.TextField()
    caratula = models.FileField(max_length=128, blank=True, verbose_name='Imagen de carátula')
    foto = models.FileField(max_length=128, blank=True, verbose_name='Foto del autor')
    idnarracion = models.AutoField(primary_key=True)
    orden = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        managed = True
        db_table = 'narracion'
        verbose_name_plural = 'Narraciones'

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    @staticmethod
    def prefijo_url():
        return 'narracion'


class NarracionImagen(models.Model):
    idarticuloimagen = models.AutoField(primary_key=True)
    imagen = models.FileField(max_length=128)
    texto = models.CharField(max_length=45)
    narracion = models.ForeignKey(Narracion, models.DO_NOTHING, db_column='idnarracion', default=0)

    class Meta:
        managed = True
        db_table = 'narracion_imagen'
