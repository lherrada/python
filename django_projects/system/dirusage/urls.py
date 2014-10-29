from django.conf.urls import patterns,url
from dirusage import views

urlpatterns = patterns('',
    url(r'^dir=(?P<dirpath>.*)$', views.dirinfo, name='dirinfo'),
)
