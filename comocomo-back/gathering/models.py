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

    def __str__(self):
        return u'{}'.format(self.name)

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
