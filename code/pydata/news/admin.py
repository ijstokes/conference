from django.contrib import admin
from news.models    import NewsItem

# Create your models here.
class NewsItemAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'title', 'date', 'author', 'publish', 'conference')
    list_editable   = ('title', 'date', 'author', 'publish', 'conference')
    list_filter     = ('author', 'date', 'publish', 'conference')
    ordering        = ('date',)
    search_fields   = ('title', 'content')

admin.site.register(NewsItem, NewsItemAdmin)

