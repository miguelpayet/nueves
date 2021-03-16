from django.db import models


class Contenido(models.Model):
    autor = models.CharField(max_length=128, blank=True, null=True, default="")
    clase = models.CharField(max_length=45, blank=True, null=True)
    contenido = models.TextField()
    imagen = models.FileField(max_length=128, blank=True, verbose_name='Imagen cabecera del artículo')
    pagina = models.ForeignKey('opciones.Pagina', models.DO_NOTHING, db_column='idpagina', default=0)
    titulo = models.CharField(max_length=128, blank=False, null=False, default="")

    class Meta:
        abstract = True
