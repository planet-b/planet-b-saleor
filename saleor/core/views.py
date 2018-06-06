import json

from django.contrib import messages
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy
from impersonate.views import impersonate as orig_impersonate

from ..account.models import User
from ..dashboard.views import staff_member_required
from ..product.utils import products_for_homepage, products_with_availability
from ..initiatives.utils import initiatives_for_homepage
from ..initiatives.utils import initiative_about_categories
from ..initiatives.utils import initiative_sort_methods
from ..seo.schema.webpage import get_webpage_schema

container_class = None

def home(request):
    products = products_for_homepage()[:8]
    products = products_with_availability(
        products, discounts=request.discounts, local_currency=request.currency)
    webpage_schema = get_webpage_schema(request)
    return TemplateResponse(
        request, 'home.html', {
            'container_class':container_class,
            'parent': None,
            'products': products,
            'webpage_schema': json.dumps(webpage_schema)})

def about(request):
    return TemplateResponse(
        request, 'brands.html',
        {
            'container_class':container_class
        }
    )

def brands(request):
    return TemplateResponse(
        request, 'brands.html',
        {
            'container_class':container_class
        }
    )

def initiatives(request):
    initiatives = initiatives_for_homepage()
    categories = initiative_about_categories()
    sortMethods = initiative_sort_methods()
    container_class = 'initiatives'
    return TemplateResponse(
        request, 'initiatives.html',
        {
            'initiatives' : initiatives,
            'container_class' : container_class,
            'categories' : categories,
            'sortMethods' : sortMethods
        }
    )

@staff_member_required
def styleguide(request):
    return TemplateResponse(request, 'styleguide.html')


def impersonate(request, uid):
    response = orig_impersonate(request, uid)
    if request.session.modified:
        msg = pgettext_lazy(
            'Impersonation message',
            'You are now logged as {}'.format(User.objects.get(pk=uid)))
        messages.success(request, msg)
    return response


def handle_404(request, exception=None):
    return TemplateResponse(request, '404.html', status=404)


def manifest(request):
    return TemplateResponse(
        request, 'manifest.json', content_type='application/json')
