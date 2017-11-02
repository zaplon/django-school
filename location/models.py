from django.db import models
from django.utils.translation import ugettext as _

LOCATION_TYPES = (('classroom', _('Classroom')), ('gym', _('Gym')))


class Place(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('name'))
    description = models.CharField(max_length=1024, verbose_name=_('description'))


class Building(Place):
    pass


class Location(Place):
    type = models.CharField(choices=LOCATION_TYPES, default='classroom', max_length=16)
    capacity = models.IntegerField(default=0, verbose_name=_('Capacity'))
    building = models.ForeignKey(Building, blank=True, null=True)

