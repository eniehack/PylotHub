from django.conf.urls import url
from . import views

app_name = 'plot'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.create_plot),
    url(r'^(?P<plot_id>[0-9a-z]+)/', views.view_plot),
    url(r'^(?P<plot_id>[0-9a-z]+)/edit/$', views.edit_plot),
    url(r'^search/$', views.search_plot)
]