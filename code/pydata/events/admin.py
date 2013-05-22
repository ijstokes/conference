from django.contrib import admin
from django.db import models

from events.models import Conference

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'location', 'begin_date', 'end_date')
    list_editable   = ('title', 'location', 'begin_date', 'end_date')
    list_filter     = ('location',)
    ordering        = ('begin_date',)
    search_fields   = ('name', 'title', 'location')

admin.site.register(Conference, ConferenceAdmin)
