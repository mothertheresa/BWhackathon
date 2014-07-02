from django.conf.urls import patterns, url, include
from Napper.views import homepage, current_datetime, hours_ahead

urlpatterns = patterns('',
    url(r'^$', homepage),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),

    # ...
)