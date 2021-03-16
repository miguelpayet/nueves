from django.db import models

from . import Contenido


class Articulo(Contenido):
    idarticulo = models.AutoField(primary_key=True)
    subtitulo = models.CharField(max_length=256, blank=True, null=True, default="")
    sumilla = models.TextField()

    class Meta:
        managed = True
        db_table = 'articulo'

    def __str__(self):
        return "%s" % self.autor

    def __unicode__(self):
        return u'%s' % self.autor

    @staticmethod
    def prefijo_url():
        return 'articulo'


class ArticuloImagen(models.Model):
    articulo = models.ForeignKey(Articulo, models.DO_NOTHING, db_column='idarticulo', default=0)
    idarticuloimagen = models.AutoField(primary_key=True)
    imagen = models.FileField(max_length=128)
    texto = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'articulo_imagen'
