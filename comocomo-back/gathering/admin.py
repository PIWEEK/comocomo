from django.contrib import admin
from .models import *


class FoodKindAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_name')

admin.site.register(FoodKind, FoodKindAdmin)


class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'nutriscore')

admin.site.register(FoodType, FoodTypeAdmin)


class DaySlotAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('user', 'date', 'slot',)
    list_filter = ('slot',)
    filter_horizontal = ('eaten',)

admin.site.register(DaySlot, DaySlotAdmin)

