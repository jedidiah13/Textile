from django.conf.urls import patterns, url, include
from webstore import views
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^category/(?P<id>.*)/$', views.webstore, name='webstore'),
    url(r'^category/(?P<id>[\w\s]+)/(?P<directory>[\w]+)/(?P<image_name>[\w]+\.[\w]+)$',views.getImage),
    url(r'^search/autocomplete/$', views.autocomplete, name='autocomplete'),
    url(r'^searchStore/$',views.searchStore, name='searchStore'),
<<<<<<< HEAD
    url(r'^query/$', include('haystack.urls'))
    
=======
    url(r'^addToCart/(?P<itemKey>[\d]+)/(?P<quantity>[\d]+)$',views.addToCart,name='addToCart'),
    url(r'^removeFromCart/(?P<itemKey>[\d]+)$',views.removeFromCart,name='removeFromCart'),
	url(r'^deleteCart/$', views.deleteCart, name='deleteCart'),
>>>>>>> FETCH_HEAD
) 
