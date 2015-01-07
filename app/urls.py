from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^/?$', 'app.views.index', name='index'),
    url(r'^artifacts/?$', 'app.views.artifacts', name='artifacts'),
    url(r'data/artifact/?$', 'app.views.data_artifact', name='data_artifact'),
    url(r'^admin/', include(admin.site.urls)),
)
