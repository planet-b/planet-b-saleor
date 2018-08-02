from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
from django.views.i18n import JavaScriptCatalog, set_language
from graphene_django.views import GraphQLView

from .account.urls import urlpatterns as account_urls
from .cart.urls import urlpatterns as cart_urls
from .checkout.urls import urlpatterns as checkout_urls
from .core.sitemaps import sitemaps
from .core.urls import urlpatterns as core_urls
from .dashboard.urls import urlpatterns as dashboard_urls
from .data_feeds.urls import urlpatterns as feed_urls
from .graphql.api import schema
from .order.urls import urlpatterns as order_urls
from .page.urls import urlpatterns as page_urls
from .product.urls import urlpatterns as product_urls
from .search.urls import urlpatterns as search_urls

handler404 = 'saleor.core.views.handle_404'

urlpatterns = [
    url(r'^.*', include('landing.urls'))]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        # static files (images, css, javascript, etc.)
        url(r'^static/(?P<path>.*)$', serve)] + static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
