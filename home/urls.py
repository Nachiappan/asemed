from django.conf.urls.defaults import *

urlpatterns = patterns('home.views',
    url('^$', 'index', name='home'),
)
