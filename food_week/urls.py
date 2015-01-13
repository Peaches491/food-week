from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns("",
    url(r'^recipes/', include('recipes.urls', namespace="recipe")),
    url(r'^admin/', include(admin.site.urls)),
)