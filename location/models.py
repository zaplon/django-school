from django.db import models
from django.utils.translation import ugettext as _

LOCATION_TYPES = (('classroom', _('Classroom')), ('gym', _('Gym')))


class Location(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('name'))
    type = models.CharField(choices=LOCATION_TYPES, default='classroom', max_length=16)
    capacity = models.IntegerField(default=0, verbose_name=_('Capacity'))

