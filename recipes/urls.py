from django.conf.urls import patterns, url
from recipes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipe_id>\d+)/$', views.detail, name='detail'),
)