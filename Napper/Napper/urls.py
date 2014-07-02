from django.conf.urls import patterns, url, include
from Napper.views import homepage

urlpatterns = patterns('',
    url(r'^$', homepage),
    # ...
)