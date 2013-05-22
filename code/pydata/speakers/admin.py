from django.contrib import admin

from speakers.models import Speaker, Presentation
from events.models import Conference

class SpeakerAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name', 'organization')
    list_editable   = ('name', 'organization')
    ordering        = ('name', 'organization')
    search_fields   = ('name', 'bio', 'organization')

admin.site.register(Speaker, SpeakerAdmin)

class PresentationAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'title', 'get_speakers_str', 'active')
    list_editable   = ('title', 'active')
    list_filter     = ('conference', 'active')
    ordering        = ('speaker__name', 'title')
    search_fields   = ('title', 'abstract', 'additional_info', 'speaker__name', 'speaker__organization')
    save_as         = True

admin.site.register(Presentation, PresentationAdmin)

