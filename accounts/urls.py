from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'signin/', views.signin_view),
    url(r'signup/', views.signup_view),
]