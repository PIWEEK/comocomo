# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import *


class FoodKindAdmin(admin.ModelAdmin):
    pass

admin.site.register(FoodKind, FoodKindAdmin)


class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind',)

admin.site.register(FoodType, FoodTypeAdmin)


class DaySlotAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('user', 'date', 'slot_name',)
    list_filter = ('slot_name',)
    filter_horizontal = ('eaten',)

admin.site.register(DaySlot, DaySlotAdmin)
