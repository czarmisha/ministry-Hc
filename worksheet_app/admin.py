from django.contrib import admin
from .models import *

# class WorkSheetAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'is_moderation', 'is_archive', 'is_paid', 'pub_date', 'current_user')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     # list_editable = ('pub_date',)
#     list_filter = ('is_moderation', 'category', 'current_user', 'is_archive')
#     # fields = ('title', 'category', 'is_archive', 'is_moderation')
#     # readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')

# admin.site.register(WorkSheet, WorkSheetAdmin)
admin.site.register(WorkSheet)
admin.site.register(Status)
admin.site.register(Region)
admin.site.register(District)