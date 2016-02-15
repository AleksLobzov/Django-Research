from django.conf.urls import include, url, patterns
from django.contrib import admin

import books.views as bv

urlpatterns = patterns('',
  url(r'^books/', include('books.urls')),
#  Для размещения приложения в корне
#  url(r'^', include('books.urls')),
  url(r'^admin/', admin.site.urls),
)
