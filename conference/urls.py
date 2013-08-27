from django.conf.urls import patterns, include, url
from sessions.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', homepage_view),
  url(r'^propose-session/$', propose_session),
  url(r'^submit-session/$', submit_session),
  url(r'^session/thanks/$', session_thanks),
)
