from django.db import models

from . import Contenido


class Video(Contenido):
    direccion = models.URLField()
    idvideo = models.AutoField(primary_key=True)
    subtitulo = models.CharField(max_length=256, blank=True, null=True, default="")

    class Meta:
        managed = True
        db_table = 'video'

    def __str__(self):
        return "%s" % self.subtitulo

    def __unicode__(self):
        return u'%s' % self.subtitulo

    @staticmethod
    def prefijo_url():
        return 'video'
