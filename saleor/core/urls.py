from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^style-guide/', views.styleguide, name='styleguide'),
    url(r'^brands/$', views.brands, name='brands'),
    url(r'^about/$', views.about, name='about'),
    url(r'^impersonate/(?P<uid>\d+)/', views.impersonate,
        name='impersonate-start'),
]
