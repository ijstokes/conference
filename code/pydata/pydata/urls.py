from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pydata.views.home', name='home'),
    # url(r'^pydata/', include('pydata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^speakers/propose/view$', 'speakers.views.view_proposal'),
    url(r'^speakers/propose/view/(?P<id>.+)$', 'speakers.views.view_proposal'),
    url(r'^speakers/propose/edit/(?P<id>.+)$', 'speakers.views.submit_proposal'),
    url(r'^speakers/propose/$', 'speakers.views.submit_proposal'),


    url(r'^(?:[a-zA-Z]{2}\d{4}/)*sponsor/sponsors$', 'sponsors.views.show_all_sponsors'),
    url(r'^(?:[a-zA-Z]{2}\d{4}/)*sponsor/info$', 'sponsors.views.sponsor_info'),

    url(r'^$', 'pages.views.wrap_page', {'page': 'home'}),
    url(r'^(?P<conf>[a-zA-Z]{2}\d{4})/(?P<conf_style>[a-zA-Z]{2}\d{4})/(?P<page>.+)/$', 'pages.views.wrap_page'),
    url(r'^(?P<conf>[a-zA-Z]{2}\d{4})/(?P<page>.+)/$', 'pages.views.wrap_page'),
    url(r'^(?P<page>.+)/$', 'pages.views.wrap_page')
)

urlpatterns += staticfiles_urlpatterns()
