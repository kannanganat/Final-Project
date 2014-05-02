from django.conf.urls import patterns, url

from genemap import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^selectinteractions$',views.selectinteractions,name='selectinteractions'),
    url(r'^getinteraction',views.getinteractions,name='getinteractions'),
    url(r'^ribosomalmapping',views.ribosomalmapping,name='ribosomalmapping')                   
)
