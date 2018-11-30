from django.conf.urls import url
from . import views

app_name = 'plot'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.create_plot, name='create'),
    url(r'^search/$', views.search_plot, name='search'),
    url(r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.view_plot, name='details'),
    url(r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/edit/$', views.edit_plot),
]
