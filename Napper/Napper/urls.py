from django.conf.urls import patterns, url, include
from Napper.views import hello

urlpatterns = patterns('',
    url(r'^hello/$', hello),
)