from schedule.models import Section, SectionDay, TimeSlot, RoomUseType, Room
from schedule.models import Track, ScheduledItemType, ScheduledItem
from django.contrib import admin

admin.site.register(Section)
admin.site.register(SectionDay)
admin.site.register(TimeSlot)
admin.site.register(RoomUseType)
admin.site.register(Room)
admin.site.register(Track)
admin.site.register(ScheduledItemType)
admin.site.register(ScheduledItem)

