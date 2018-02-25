from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.red),#Redirect from startpage
    url(r'^admin/', admin.site.urls),#standart adminpanel
    url(r'^index/', include('index.urls')),#index app
    url(r'^metrics/', include('metrics.urls')),#metrics app
    url(r'^auth/', include('auth.urls')),#auth app
    url(r'^books/', include('books.urls')),#books app
]
