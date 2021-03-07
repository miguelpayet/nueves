from django.db import models


class Pagina(models.Model):
    idpagina = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=512, default="")
    direccion = models.CharField(max_length=255, blank=True)
    nombre = models.CharField(max_length=45, default="")
    titulo = models.CharField(max_length=45, default="")

    def __str__(self):
        return '%s' % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'pagina'
        managed = True
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
