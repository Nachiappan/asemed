from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('accounts.urls')),
    (r'^diseases/', include('diseases.urls')),
    (r'^appointments/', include('appointments.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'', include('home.urls')),
)
