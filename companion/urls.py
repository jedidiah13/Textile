from django.conf.urls import patterns, url
from companion import views


urlpatterns = patterns('',
    url(r'^(?P<id>.*)/', views.companion, name='companion')

)
