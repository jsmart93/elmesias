from django.conf.urls import url, include
from . import views

app_name = 'about'
urlpatterns = [
    url(r'^$', views.about, name='about'),
]
