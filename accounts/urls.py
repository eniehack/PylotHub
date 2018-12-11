from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'signin/', views.signin_view, name='signin'),
    url(r'signup/', views.signup_view, name='signup'),
    url(r'signout/', views.signout_view, name='signout'),
]
