from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from comocomo.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comocomo.views.home', name='home'),
    # url(r'^comocomo/', include('comocomo.foo.urls')),
    url(r'^week/$', WeekView.as_view(), name='week'),
    url(r'^week/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', WeekView.as_view(), name='week'),
    url(r'^slot/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slot>\d{1})/$', SlotView.as_view(), name='slot'),
    url(r'^food_kinds/$', FoodKindsView.as_view(), name='food_kinds'),
    url(r'^food_types/$', FoodTypesView.as_view(), name='food_types'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

