from django.db import models


class Opcion(models.Model):
    idopcion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, default="")
    padre = models.ForeignKey('Opcion', on_delete=models.CASCADE, db_column='idpadre', to_field='idopcion', blank=True)
    pagina = models.ForeignKey('Pagina', on_delete=models.DO_NOTHING, db_column='idpagina')
    posicion = models.IntegerField(unique=True)
    tipo = models.IntegerField(verbose_name='Tipo (1 = Opción, 2 = Subopción)', default=1)
    titulo = models.CharField(max_length=45, default="", blank=False, null=False)

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'opcion'
        managed = True
        verbose_name = 'Opción'
        verbose_name_plural = 'Opciones'
