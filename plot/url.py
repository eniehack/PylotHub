from django.conf.urls import url
from . import views

app_name = 'plot'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.create_plot),
    url(r'^(<plot_id>\d+)/', views.view_plot),
    url(r'^(?P<plot_id>\d+)/edit/$', views.edit_plot),
    url(r'^search/$', views.search_plot)
]