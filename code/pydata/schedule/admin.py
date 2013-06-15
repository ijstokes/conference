from django.contrib import admin

from schedule.models import Section, SectionDay, TimeSlot, RoomUseType, Room
from schedule.models import Track, ScheduledItemType, ScheduledItem
from speakers.models import Presentation
from events.models   import Conference

class SectionAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name', 'start_day', 'end_day', 'conference')
    list_editable   = ('name', 'start_day', 'end_day', 'conference')
    list_filter     = ('start_day', 'end_day', 'conference')
    ordering        = ('start_day', 'end_day', 'conference', 'id')
    search_fields   = ('name',)
    save_as         = True


admin.site.register(Section, SectionAdmin)

class TrackAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name', 'conference')
    list_editable   = ('name', 'conference')
    list_filter     = ('name', 'conference')
    ordering        = ('conference', 'name', 'id')
    search_fields   = ('name',)
    save_as         = True

admin.site.register(Track, TrackAdmin)

class TimeSlotAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'sectionDay', 'start_time', 'end_time', 'conference')
    list_editable   = ('start_time', 'end_time', 'sectionDay', 'conference')
    list_filter     = ('sectionDay', 'conference')
    ordering        = ('conference', 'sectionDay', 'start_time', 'end_time', 'id')
    save_as         = True

admin.site.register(TimeSlot, TimeSlotAdmin)

class SectionDayAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'section', 'day', 'conference')
    list_editable   = ('section', 'day', 'conference')
    list_filter     = ('section', 'day', 'conference')
    ordering        = ('conference', 'day', 'section', 'id')
    save_as         = True

admin.site.register(SectionDay, SectionDayAdmin)

class RoomUseTypeAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name', 'description')
    list_editable   = ('name', 'description')
    list_filter     = ('name', 'description')
    ordering        = ('name', 'description', 'id')
    search_fields   = ('name', 'description')

admin.site.register(RoomUseType, RoomUseTypeAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name', 'useType', 'capacity', 'conference')
    list_editable   = ('name', 'useType', 'capacity', 'conference')
    list_filter     = ('name', 'useType', 'conference')
    ordering        = ('conference', 'name', 'useType', 'capacity', 'id',)
    search_fields   = ('name', 'notes')
    save_as         = True

admin.site.register(Room, RoomAdmin)

class ScheduledItemAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name')
    list_editable   = ('name',)
    ordering        = ('name', 'id',)
    search_fields   = ('name',)


admin.site.register(ScheduledItemType, ScheduledItemAdmin)

class ScheduledItemAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'track', 'timeSlot', 'presentation', 'room', 'itemType', 'num_slots', 'conference')
    list_editable   = ('itemType', 'timeSlot', 'num_slots', 'track', 'room', 'presentation', 'conference')
    list_filter     = ('itemType', 'track', 'room', 'conference')
    ordering        = ('conference', 'track', 'timeSlot__sectionDay__day', 'timeSlot__start_time', 'id')
    search_fields   = ('presentation__title', 'presentation__abstract', 'presentation__additional_info', 'presentation__speaker__name', 'presentation__speaker__organization', 'room__name', 'room__notes')
    save_as         = True

admin.site.register(ScheduledItem, ScheduledItemAdmin)
