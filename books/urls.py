from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
  url(r'^authors/(?P<author_id>[0-9]+)/$', views.author_detail, name='author_detail'),
  url(r'^charts/1$', views.chart1_data, name='chart1_data'),
) 
