from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<book_id>[0-9]+)$', views.detail, name='detail'),
) 