from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^system/', include('dirusage.urls',namespace='dirusage'))
    #url(r'^admin/', include(admin.site.urls)),
)
