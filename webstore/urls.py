from django.conf.urls import patterns, url
from webstore import views
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^category/(?P<id>.*)/$', views.webstore, name='webstore'),
    url(r'^category/(?P<id>[\w\s]+)/(?P<directory>[\w]+)/(?P<image_name>[\w]+\.[\w]+)$',views.getImage),
    url(r'^search/autocomplete/$', views.autocomplete, name='autocomplete'),
    
) 
