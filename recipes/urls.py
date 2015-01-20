from django.conf.urls import patterns, url
from recipes import views

urlpatterns = patterns('',
    url(r'^$',                           views.index, name='index'),
    url(r'^(?P<recipe_id>\d+)/$',        views.detail, name='detail'),
    url(r'^(?P<recipe_id>\d+)/edit/$',   views.edit, name='edit'),
    url(r'^new/$',                       views.edit, name='new'),
    url(r'^(?P<recipe_id>\d+)/test/$',   views.test, name='test'),
)