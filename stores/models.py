from . import abstract_models

from django.db import models
from django.utils.translation import ugettext as _

class StoreAddress(abstract_models.StoreAddress):
    pass


class StoreGroup(abstract_models.StoreGroup):
    pass


class Store(abstract_models.Store):
    website = models.CharField(_('Website'), max_length=64, blank=True, null=True)
    payment_methods = models.CharField(_('Payment methods'), max_length=64, blank=True, null=True)
    disabled_friendly = models.BooleanField(_('Disabled-friendly'), default=False)
    baby_friendly = models.BooleanField(_('Baby-friendly'), default=False)


class OpeningPeriod(abstract_models.OpeningPeriod):
    pass


class StoreStock(abstract_models.StoreStock):
    pass
