from django.db import models


class Parametro(models.Model):
    descripcion = models.TextField(max_length=256)
    email = models.CharField(max_length=256, blank=False, null=False, verbose_name="Email de la maestría")
    idparametro = models.AutoField(primary_key=True)
    logo = models.ImageField(max_length=50, verbose_name='Logo')
    logo_maestria = models.ImageField(max_length=50, verbose_name='Logo Maestría')
    logo_pucp = models.ImageField(max_length=50, verbose_name='Logo PUCP')
    podcast = models.ImageField(max_length=50, verbose_name='Imagen Podcast')
    texto_logo = models.CharField(max_length=64, verbose_name='Texto alternativo Logo')
    texto_logo_maestria = models.CharField(max_length=64, verbose_name='Texto alternativo Logo Maestría')
    texto_logo_pucp = models.CharField(max_length=64, verbose_name='Texto alternativo Logo PUCP')
    texto_podcast = models.CharField(max_length=64, verbose_name='Texto alternativo podcast')
    url_maestria = models.CharField(max_length=256, verbose_name='Sitio web de la Maestría')
    url_pucp = models.CharField(max_length=128, verbose_name='Sitio web de la PUCP')

    def __str__(self):
        return "%s %s" % ("Parámetro", self.idparametro)

    def __unicode__(self):
        return u'%s %s' % ("Parámetro", self.idparametro)

    class Meta:
        db_table = 'parametro'
        managed = True
        verbose_name = 'Parámetro'
        verbose_name_plural = 'Parámetros'
