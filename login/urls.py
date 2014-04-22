from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
    url(r'^register/$', views.registration, name='index.html'),
    url(r'^authenticate/$', views.authenticateLogin, name='index.html'),
    url(r'^authenticateUser/$', views.authenticateUser, name='index.html'),
    url(r'^activate/(?P<confirmation_code>[\w]+)/(?P<username>[\w]+/)$', views.activate, {}, 'activate'),
    url(r'^logoutUser/$', views.logoutUser, name='logout'),
    url(r'^userInfo/$', views.userInfo, name='userInfo'),
    url(r'^changeFirstName/$', views.changeFirstName, name='userInfoChange'),
    url(r'^changeLastName/$', views.changeLastName, name='userInfoChange'),
    url(r'^changeEmail/$', views.changeEmail, name='userInfoChange'),
    url(r'^changePassword/$', views.changePassword, name='userInfoChange'),
    url(r'^changeAddress/$', views.changeAddress, name='userInfoChange'),
    url(r'^orderHistory/$', views.orderHistory, name='orderHistory')
)
