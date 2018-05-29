import datetime
from decimal import Decimal

from django.conf import settings
from django.contrib.postgres.fields import HStoreField
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.db.models import F, Max, Q
from django.dispatch import receiver
from django.urls import reverse
from django.utils.encoding import smart_text
from django.utils.text import slugify
from django.utils.translation import pgettext_lazy
from django_prices.models import MoneyField
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from text_unidecode import unidecode
from versatileimagefield.fields import PPOIField, VersatileImageField

class Initiative(models.Model):
    name = 'tacos' # models.CharField(max_length=128)
    slug = 'tacos' # models.SlugField(max_length=128)
    description = 'tacos' # models.TextField(blank=True)
    author = 'tacos' # models.CharField(max_length=128)
    location = 'tacos' # models.CharField(max_length=128)
    total_donations = 'tacos' # MoneyField(
    #     currency=settings.DEFAULT_CURRENCY, max_digits=12, decimal_places=2,
    #     blank=True, null=True)
    donation_goal = 'tacos' # MoneyField(
    #     currency=settings.DEFAULT_CURRENCY, max_digits=12, decimal_places=2,
    #     blank=True, null=True)
    donation_days_left = 'tacos' # models.PositiveIntegerField(editable=False)

    class Meta:
        app_label = 'initiative'

    def __str__(self):
        return self.name


