from django.conf.urls import patterns, url
from companion import views


urlpatterns = patterns('',
    url(r'^category/(?P<id>.*)/$', views.companion, name='companion'),
    url(r'^category/(?P<id>[\w\s]+)/(?P<directory>[\w]+)/(?P<image_name>[\w]+\.[\w]+)$',views.getImage), 
    url(r'^topic/(?P<id>.*)/$', views.topic, name='topic'),   
)
