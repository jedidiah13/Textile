from django.conf.urls import patterns, url
from webstore import views
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^category/(?P<id>.*)/$', views.webstore, name='webstore'),
    url(r'^category/(?P<id>[\w\s]+)/(?P<directory>[\w]+)/(?P<image_name>[\w]+\.[\w]+)$',views.getImage),
    url(r'^search/autocomplete/$', views.autocomplete, name='autocomplete'),
    url(r'^userInfo/$', views.userInfo, name='userInfo'),
    url(r'^userInfoChange/$', views.userInfoChange, name='userInfoChange'),
    url(r'^orderHistory/$', views.orderHistory, name='orderHistory')
)
