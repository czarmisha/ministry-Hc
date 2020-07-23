from django.contrib import admin
from .models import *

class WorkSheetAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'region', 'district', 'shifokor', 'hamshira')
    list_display_links = ('first_name',)
    search_fields = ('last_name', 'region', 'district', 'shifokor', 'hamshira',)
    list_filter = ('region', 'shifokor', 'hamshira', 'birth_date', 'district',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'soato',)
    list_display_links = ('name', 'soato',)
    search_fields = ('name', 'soato',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'soato', 'region')
    list_display_links = ('name', 'soato',)
    search_fields = ('name', 'soato',)

admin.site.register(WorkSheet, WorkSheetAdmin)
admin.site.register(Status)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)