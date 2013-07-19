from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from comocomo.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^food_kinds/$', FoodKindsView.as_view(), name='food_kinds'),
    url(r'^food_types/$', FoodTypesView.as_view(), name='food_types'),
    url(r'^week/$', WeekView.as_view(), name='week'),
    url(r'^slot/$', SlotView.as_view(), name='slot'),
    url(r'^slot_eaten/$', SlotEatenView.as_view(), name='slot_eaten'),
    url(r'^results/$', ResultsView.as_view(), name='results'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

