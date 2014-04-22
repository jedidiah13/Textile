from django.conf.urls import patterns, url
from blog import views
from login import urls

urlpatterns = patterns('',
    url(r'^$','blog.views.index'),
    url(r'^(?P<slug>[^\.]+)/$','blog.views.post'),
    
)
