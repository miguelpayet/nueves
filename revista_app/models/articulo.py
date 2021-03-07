from django.db import models


class Articulo(models.Model):
    idarticulo = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=128, blank=False, null=False, default="")
    clase = models.CharField(max_length=45, blank=True, null=True)
    contenido = models.TextField()
    imagen = models.FileField(max_length=128)
    orden = models.IntegerField(blank=False, null=False, default=0)
    pagina = models.ForeignKey('opciones.Pagina', models.DO_NOTHING, db_column='idpagina', default=0)
    titulo = models.CharField(max_length=128, blank=False, null=False, default="")

    class Meta:
        managed = True
        db_table = 'articulo'

    def __str__(self):
        return "%s" % self.autor

    def __unicode__(self):
        return u'%s' % self.autor


class ArticuloImagen(models.Model):
    idarticuloimagen = models.AutoField(primary_key=True)
    imagen = models.FileField(max_length=128)
    texto = models.CharField(max_length=45)
    articulo = models.ForeignKey('Articulo', models.DO_NOTHING, db_column='idarticulo', default=0)

    class Meta:
        managed = True
        db_table = 'articulo_imagen'
