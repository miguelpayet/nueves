from django.db import models


class Texto(models.Model):
    contenido = models.TextField()
    idtexto = models.AutoField(primary_key=True)
    imagen = models.FileField(max_length=128, blank=True, verbose_name='Imagen cabecera del artículo')
    orden = models.IntegerField(blank=False, null=False, default=0)
    texto_url = models.CharField(max_length=128, blank=True, null=True, default="", verbose_name="Texto de Enlace")
    titulo = models.CharField(max_length=128, blank=False, null=False, default="")
    url = models.CharField(max_length=128, blank=True, null=True, default="", verbose_name="Dirección de Enlace")

    class Meta:
        managed = True
        db_table = 'texto'
        verbose_name_plural = 'Textos'

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo
