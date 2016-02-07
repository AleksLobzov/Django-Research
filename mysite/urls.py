from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^books/', include('books.urls')),
  url(r'^admin/', admin.site.urls),
)
