from collections import defaultdict, namedtuple
from urllib.parse import urlencode

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db.models import F
from django.utils.encoding import smart_text
from django_prices.templatetags import prices_i18n
from prices import TaxedMoneyRange

from ..cart.utils import get_cart_from_request, get_or_create_cart_from_request
from ..core.utils import (
	ZERO_TAXED_MONEY, get_paginator_items, to_local_currency)
from ..core.utils.filters import get_now_sorted_by
from ..seo.schema.product import variant_json_ld

def initiatives_for_homepage():
	from .models import Initiative
	return [Initiative() for i in range(5)]

def initiative_sort_methods():
	from .models import Initiative_SortMethod
	dictionaries = [
		{"value":"Sort 1", "label":"Sort 1"},
		{"value":"Sort 2", "label":"Sort 2"},
		{"value":"Sort 3", "label":"Sort 3"}
	]
	sortMethods = list()
	for sort in dictionaries:
		sortMethods.append(Initiative_SortMethod(sort))
	return sortMethods

def initiative_about_categories():
	from .models import Initiative_About
	dictionaries = [
		{"value":"Category 1", "label":"Category 1"},
		{"value":"Category 2", "label":"Category 2"},
		{"value":"Category 3", "label":"Category 3"}
	]
	categories = list()
	for cat in dictionaries:
		categories.append(Initiative_About(cat))
	return categories