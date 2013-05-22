from django.contrib import admin

from sponsors.models import SponsorLevel, Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name', 'url', 'priority')
    list_editable   = ('name', 'url', 'priority')
    ordering        = ('name',)
    search_fields   = ('name', 'description')

admin.site.register(Sponsor, SponsorAdmin)

class SponsorLevelAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'name', 'min_amount', 'conference')
    list_editable   = ('name', 'min_amount', 'conference')
    list_filter     = ('conference',)
    ordering        = ('conference__name', '-min_amount',)
    search_fields   = ('name', 'description')
    save_as         = True

admin.site.register(SponsorLevel, SponsorLevelAdmin)

