# Import admin and models
from django.contrib.gis import admin
from models import *

class DoodleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DoodleAdmin(admin.GeoModelAdmin):
    field = (None, {'fields': ('name')})
    field = (None, {'fields': ('doodle')})
    field = (None, {'fields': ('doodle_date')})
    list_display = ('name', 'doodle_date', 'doodle')
    list_filter = ('name', 'doodle_date')

# Register each model with its associated admin class
admin.site.register(DoodleType, DoodleTypeAdmin)
admin.site.register(Doodle, DoodleAdmin)

