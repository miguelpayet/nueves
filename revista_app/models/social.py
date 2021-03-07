from django.db import models


class Social(models.Model):
    idsocial = models.AutoField(primary_key=True)
    direccion = models.URLField(max_length=128, blank=False, null=False, default="")
    imagen = models.FileField(max_length=128, blank=False, null=False, default="")
    nombre = models.CharField(max_length=45, blank=False, default="")
    texto = models.CharField(max_length=45, blank=False, null=False, default="")
    orden = models.IntegerField(blank=False, null=False, default=0, unique=True)

    class Meta:
        managed = True
        db_table = 'social'
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre
