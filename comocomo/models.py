# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.staticfiles.storage import staticfiles_storage

import os.path

class FoodKind(models.Model):

    ICONS_PATH = 'img/icons'

    name = models.CharField(
                blank=False, null=False, max_length=255,
                verbose_name=_(u'nombre'))

    description = models.TextField(
                blank=True, null=False,
                verbose_name=_(u'descripción'))

    icon_name = models.CharField(
                blank=False, null=False, max_length=100,
                verbose_name=_(u'nombre del icono'),
                help_text=_(u'Nombre de un fichero .png, .gif o .jpg de 32px de alto, situado en el directorio de iconos'))

    class Meta:
        verbose_name = _(u'clase de comida')
        verbose_name_plural = _(u'clases de comida')
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @property
    def icon_path(self):
        return staticfiles_storage.url(os.path.join(self.ICONS_PATH, self.icon_name))


class FoodType(models.Model):

    kind = models.ForeignKey('FoodKind',
                blank=False, null=False,
                related_name='food_types',
                verbose_name=_(u'clase'))

    name = models.CharField(
                blank=False, null=False, max_length=255,
                verbose_name=_(u'nombre'))

    description = models.TextField(
                blank=True, null=False,
                verbose_name=_(u'descripción'))

    min_week = models.PositiveSmallIntegerField(
                blank=False, null=False,
                verbose_name=_(u'mínimo semanal'),
                help_text=_(u'Mínimo nº de raciones que habría que consumir por semana'))

    max_week = models.PositiveSmallIntegerField(
                blank=False, null=False,
                verbose_name=_(u'máximo semanal'),
                help_text=_(u'Máximo nº de raciones que habría que consumir por semana'))

    avg_price = models.DecimalField(
                blank=False, null=False, max_digits=5, decimal_places=2,
                verbose_name=_(u'precio medio'),
                help_text=_(u'Precio medio de una ración'))

    dev_price = models.DecimalField(
                blank=False, null=False, max_digits=5, decimal_places=2,
                verbose_name=_(u'desviación del precio medio'),
                help_text=_(u'Valor típico de desviación de precio arriba y abajo'))

    eco_level = models.PositiveSmallIntegerField(
                blank=False, null=False,
                verbose_name=_(u'nivel ecológico'),
                help_text=_(u'Indicador de 1 (muy malo) a 5 (estupendo) de la calidad ecológica'))

    social_level = models.PositiveSmallIntegerField(
                blank=False, null=False,
                verbose_name=_(u'nivel social'),
                help_text=_(u'Indicador de 1 (muy malo) a 5 (estupendo) de la calidad social'))

    class Meta:
        verbose_name = _(u'tipo de comida')
        verbose_name_plural = _(u'tipos de comida')
        ordering = ('kind', 'name')

    def __unicode__(self):
        return u'{} {}'.format(self.kind.name, self.name)


class SlotType:
    BREAKFAST = 1
    MID_MORNING = 2
    LUNCH = 3
    MID_EVENING = 4
    DINNER = 5

    @classmethod
    def values(cls):
        values_list = [getattr(cls, attr) for attr in dir(cls) if attr[0].isupper()]
        values_list.sort()
        return values_list


class DaySlot(models.Model):

    SLOT_CHOICES = (
        (SlotType.BREAKFAST, _(u'Desayuno')),
        (SlotType.MID_MORNING, _(u'Media mañana')),
        (SlotType.LUNCH, _(u'Comida')),
        (SlotType.MID_EVENING, _(u'Merienda')),
        (SlotType.DINNER, _(u'Cena')),
    )

    user = models.ForeignKey('auth.User',
                blank=False, null=False,
                verbose_name=_(u'usuario'))

    date = models.DateField(
                blank=False, null=False,
                verbose_name=_(u'fecha'))

    slot = models.PositiveSmallIntegerField(
                blank=False, null=False,
                choices=SLOT_CHOICES,
                verbose_name=_(u'período'))

    eaten = models.ManyToManyField('FoodType',
                blank=False,
                verbose_name=_(u'comidas'),
                help_text=_(u'Qué tipos de comida has comido en este período'))


    class Meta:
        verbose_name = _(u'comida registrada')
        verbose_name_plural = _(u'comidas registradas')
        unique_together = ('user', 'date', 'slot')
        ordering = ('user', 'date', 'slot')

    def slot_name(self):
        for id, name in self.SLOT_CHOICES:
            if self.slot == id:
                return unicode(name)
        return unicode(_(u'período no definido'))

    def __unicode__(self):
        return u'({0}) {1} - {2}'.format(
            self.user.username,
            self.date.strftime('%d/%m/%Y'),
            self.slot_name(),
        )


class EatingProfile(models.Model):

    name = models.CharField(
                blank=False, null=False, max_length=255,
                verbose_name=_(u'nombre'))

    description = models.TextField(
                blank=True, null=False,
                verbose_name=_(u'descripción'))

    class Meta:
        verbose_name = _(u'perfil de alimentación')
        verbose_name_plural = _(u'perfiles de alimentación')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class EatingProfileItem(models.Model):

    profile = models.ForeignKey('EatingProfile',
                blank=False, null=False,
                related_name='items',
                verbose_name=_(u'perfil'))

    date = models.DateField(
                blank=False, null=False,
                verbose_name=_(u'fecha'))

    slot = models.PositiveSmallIntegerField(
                blank=False, null=False,
                choices=DaySlot.SLOT_CHOICES,
                verbose_name=_(u'período'))

    eaten = models.ManyToManyField('FoodType',
                blank=False,
                verbose_name=_(u'comidas'),
                help_text=_(u'Qué tipos de comida has comido en este período'))

    class Meta:
        verbose_name = _(u'ítem de perfil')
        verbose_name_plural = _(u'ítems de perfil')
        unique_together = ('profile', 'date', 'slot')
        ordering = ('profile', 'date', 'slot')

    def __unicode__(self):
        return self.name

