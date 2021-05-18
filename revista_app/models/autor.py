from django.db import models


class Autor(models.Model):
    biografia = models.TextField()
    foto = models.FileField(max_length=128, blank=True, verbose_name='Foto del autor')
    idautor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, blank=False, verbose_name='Nombre del autor');

    class Meta:
        managed = True
        db_table = 'autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre
