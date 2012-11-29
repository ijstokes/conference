from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pydata.views.home', name='home'),
    # url(r'^pydata/', include('pydata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/(?P<page>[^/]+)/$','pages.views.wrap_page'),
    url(r'^pages/(?P<conf>[^/]+)/(?P<page>[^/]+)/$','pages.views.wrap_page'),
    url(r'^pages/(?P<conf>[^/]+)/(?P<conf_style>[^/]+)/(?P<page>[^/]+)/$','pages.views.wrap_page'),
)

urlpatterns += staticfiles_urlpatterns()
