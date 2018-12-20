from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.staticfiles.storage import staticfiles_storage

import os.path

class FoodKind(models.Model):

    ICONS_PATH = 'gathering/img/icons'

    name = models.CharField(
                blank=False, null=False, max_length=255,
                verbose_name=_('nombre'))

    description = models.TextField(
                blank=True, null=False,
                verbose_name=_('descripción'))

    icon_name = models.CharField(
                blank=False, null=False, max_length=100,
                verbose_name=_('nombre del icono'),
                help_text=_('Nombre de un fichero .png, .gif o .jpg de 32px de alto, situado en el directorio de iconos'))

    class Meta:
        verbose_name = _('grupo de comida')
        verbose_name_plural = _('grupos de comida')
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def icon_path(self):
        return staticfiles_storage.url(os.path.join(self.ICONS_PATH, self.icon_name))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon_path': self.icon_path,
        }


class FoodType(models.Model):

    NUTRISCORE_CHOICES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]

    kind = models.ForeignKey('FoodKind',
                blank=False, null=False,
                on_delete=models.CASCADE,
                related_name='food_types',
                verbose_name=_('grupo'))

    name = models.CharField(
                blank=False, null=False, max_length=255,
                verbose_name=_('nombre'))

    nutriscore = models.CharField(
                blank=False, null=False, max_length=1,
                choices=NUTRISCORE_CHOICES,
                verbose_name=_('nutriscore'))

    class Meta:
        verbose_name = _('tipo de comida')
        verbose_name_plural = _('tipos de comida')
        ordering = ('kind', 'name')

    def __str__(self):
        return '{} {}'.format(self.kind.name, self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'kind_id': self.kind.id,
            'name': self.name,
            'nutriscore': self.nutriscore,
        }


class SlotType:
    BREAKFAST = 0
    MID_MORNING = 1
    LUNCH = 2
    MID_EVENING = 3
    DINNER = 4

    @classmethod
    def values(cls):
        values_list = [getattr(cls, attr) for attr in dir(cls) if attr[0].isupper()]
        values_list.sort()
        return values_list


class FoodRegistration(models.Model):

    SLOT_CHOICES = (
        (SlotType.BREAKFAST, _('Desayuno')),
        (SlotType.MID_MORNING, _('Media mañana')),
        (SlotType.LUNCH, _('Comida')),
        (SlotType.MID_EVENING, _('Merienda')),
        (SlotType.DINNER, _('Cena')),
    )

    user = models.ForeignKey('auth.User',
                blank=False, null=False,
                on_delete=models.CASCADE,
                verbose_name=_('usuario'))

    date = models.DateField(
                blank=False, null=False,
                verbose_name=_('fecha'))

    slot = models.PositiveSmallIntegerField(
                blank=False, null=False,
                choices=SLOT_CHOICES,
                verbose_name=_('período'))

    eaten = models.ManyToManyField('FoodType',
                blank=False,
                verbose_name=_('comidas'),
                help_text=_('Qué tipos de comida has comido en este período'))


    class Meta:
        verbose_name = _('comida registrada')
        verbose_name_plural = _('comidas registradas')
        unique_together = ('user', 'date', 'slot')
        ordering = ('user', 'date', 'slot')

    def slot_name(self):
        for id, name in self.SLOT_CHOICES:
            if self.slot == id:
                return name
        return _('período no definido')

    def __str__(self):
        return '({0}) {1} - {2}'.format(
            self.user.username,
            self.date.strftime('%d/%m/%Y'),
            self.slot_name(),
        )

    def to_dict(self):
        return {
            'date': self.date,
            'slot': self.slot,
            'eaten': [food_type.to_dict() for food_type in self.eaten.all()],
        }

