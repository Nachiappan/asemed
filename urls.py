from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^diseases/', include('diseases.urls')),
    (r'^appointments/', include('appointments.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT, 'show_indexes':True}),
    (r'', include('home.urls')),
)
