from django.conf.urls import patterns, include, url
from conference.views import homepage_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', homepage_view)
)
