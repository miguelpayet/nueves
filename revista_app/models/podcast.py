from django.db import models


class Podcast(models.Model):
    idpodcast = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=512, verbose_name="Descripción del podcast")
    sumilla = models.TextField(max_length=512, verbose_name="Sumilla de introducción al podcast")
    direccion = models.CharField(max_length=256, blank=False, null=False,
                                 verbose_name="Dirección del podcast para suscripción")
    link = models.CharField(max_length=256, verbose_name='Dirección del episodio actual del podcast')
    titulo = models.CharField(max_length=256, verbose_name="Título del podcast")

    def __str__(self):
        return "%s %s" % ("Parámetro", self.idpodcast)

    def __unicode__(self):
        return u'%s %s' % ("Parámetro", self.idpodcast)

    class Meta:
        db_table = 'podcast'
        managed = True
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcasts'
