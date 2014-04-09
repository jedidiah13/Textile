from django.conf.urls import patterns, include, url
from django.contrib import admin
from login import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogadmin/', include(admin.site.urls)),
    url(r'^', include('frontend.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^webstore/', include('webstore.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^companion/', include('companion.urls'))
#    url(r'^register/$',views.addUser, name='registration'),
#    url(r'^authenticate/$', views.authenticateLogin, name='authenticateLogin')

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
