from django.conf.urls import url, include
from . import views

app_name = 'prayer_request'
urlpatterns = [
    url(r'^$', views.prayer_request, name='prayer_request'),
    url(r'^send/$', views.send, name='send'),
]
