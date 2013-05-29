from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^.*\.js$', 'pages.views.java_script'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/?$',                  'pages.views.wrap_page'),
    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*sponsor/sponsors$',  'sponsors.views.show_all_sponsors'),
    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*sponsor/info$',      'sponsors.views.sponsor_info'),


    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*schedule/(?P<sectionday>\d\d?)$', 'schedule.views.show_schedule_sectionDay'),
    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*schedule/$',         'schedule.views.show_schedule_all'),


    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*speakers/$',         'speakers.views.view_speakers'),
    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*abstracts/$',        'speakers.views.view_abstracts'),
    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*keynotes/$',         'speakers.views.view_keynotes'),


    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/*news/$',             'news.views.view_news'),

    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/about/(?P<page>.+)/$', 'pages.views.wrap_page',{'about':'about'}),
    url(r'^(?P<conference>[a-zA-Z]{2,3}\d{4})/(?P<page>.+)/$',      'pages.views.wrap_page'),

    url(r'^(?P<page>.+)/$',                                         'pages.views.common'),
    url(r'^/?$',                                         			'pages.views.common'),
)

urlpatterns += staticfiles_urlpatterns()
