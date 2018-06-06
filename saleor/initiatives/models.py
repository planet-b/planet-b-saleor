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

class Initiative_SortMethod(models.Model):

    class Meta:
        app_label = 'sort'

    def __init__(self, obj):
        self.value = obj['value']
        self.label = obj['label']
        self.name = obj['value']

    def __str__(self):
        return self.name

class Initiative_About(models.Model):

    class Meta:
        app_label = 'about'

    def __init__(self, obj):
        self.value = obj['value']
        self.label = obj['label']
        self.name = obj['value']

    def __str__(self):
        return self.name

class Initiative(models.Model):
    slug = 'tacos' # models.SlugField(max_length=128)
    name = 'Haiti Earth Quake Initiative' # models.CharField(max_length=128)
    description = 'Does the thing' # models.TextField(blank=True)
    author_first_name = 'Steve' # models.CharField(max_length=128)
    author_last_name = 'Billy' # models.CharField(max_length=128)
    location_city = 'City' # models.CharField(max_length=128)
    location_state = 'State' # models.CharField(max_length=128)
    location_country = 'Haiti' # models.CharField(max_length=128)
    total_donations = '100,000' # MoneyField(
    #     currency=settings.DEFAULT_CURRENCY, max_digits=12, decimal_places=2,
    #     blank=True, null=True)
    donation_goal = '400,000' # MoneyField(
    #     currency=settings.DEFAULT_CURRENCY, max_digits=12, decimal_places=2,
    #     blank=True, null=True)
    goal_percentage = 25;
    initiative_category = 'Natural Disasters'
    background_image_url = '/static/images/initiatives/forestFire.jpg'
    donation_days_left = 5 # models.PositiveIntegerField(editable=False)

    class Meta:
        app_label = 'initiative'

    def __str__(self):
        return self.name


