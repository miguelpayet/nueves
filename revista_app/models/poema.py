from django.db import models


class Poema(models.Model):
    autor = models.ForeignKey('Autor', on_delete=models.DO_NOTHING, db_column='idautor')
    clase = models.CharField(max_length=45, blank=True, null=True)
    contenido = models.TextField()
    idpoema = models.AutoField(primary_key=True)
    imagen = models.FileField(max_length=128, blank=True, verbose_name='Imagen cabecera del artículo')
    orden = models.IntegerField(blank=False, null=False, default=0)
    titulo = models.CharField(max_length=128, blank=False, null=False, default="")

    class Meta:
        managed = True
        db_table = 'poema'
        verbose_name_plural = 'Poemas'

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    @staticmethod
    def prefijo_url():
        return 'np'
