from django.contrib import admin
from django.contrib.gis import admin
from data.models import Incident, Agency, AlarmLevel, FireBlock, CensusBlock

# Register your models here.
admin.site.register(Incident)
admin.site.register(Agency)
admin.site.register(AlarmLevel)
admin.site.register(FireBlock, admin.OSMGeoAdmin)
admin.site.register(CensusBlock, admin.OSMGeoAdmin)
