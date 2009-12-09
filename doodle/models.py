from django.db import models

# Create your models here.

# import GeoDjango stuff to support spatial data typse
from django.contrib.gis.db import models

# use python time goodies
import datetime

class Doodle(models.Model):
    name = models.CharField(max_length=255)
    doodle = models.LineStringField(srid=27562, null=True, blank=True)
    doodle_date = models.DateTimeField('DateAdded', \
                                       auto_now=True, \
                                       auto_now_add=False)
    objects = models.GeoManager()

    class Meta:
        db_table = 'doodle'
        verbose_name = ('Doodle')
        verbose_name_plural = ('Doodle')
        ordering = ('doodle_date', )
