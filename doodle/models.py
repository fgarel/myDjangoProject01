# Our base class
from django.db import models
# Import GeoDjango stuff to support spatial data typse
from django.contrib.gis.db import models
# Use python time goodies
import datetime

# A class for the choices option
class DoodleType(models.Model):
    # Create a name field
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'doodletype'
        verbose_name = ('Doodle Type')
        verbose_name_plural = ('Doodle Types')
        ordering = ('name',)

# A class defines our model if it inherits from models.model
class Doodle(models.Model):
    type = models.ForeignKey(DoodleType)
    # Create a name field
    name = models.CharField(max_length=255)
    # And a geometry fiels for our doodle
    doodle = models.LineStringField(srid=27562, null=True, blank=True)
    # Lastly make au auto populated date field
    doodle_date = models.DateTimeField('DateAdded', \
                                       auto_now=True, \
                                       auto_now_add=False)
    # Model manager that must be added to any model with a geometry
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
   
    # Metadata inner class
    class Meta:
        # Name the table should be given on the database backend (optional)
        db_table = 'doodle'
        # Name to be used in the user interface (generated web pages) for this model
        verbose_name = ('Doodle')
        # Plural name to be used in the user interface
        verbose_name_plural = ('Doodle')
        # Column ordering to be used by default if a collection of
        # model instances is obtained
        ordering = ('doodle_date', )

