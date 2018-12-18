from django.conf.urls import url, include

app_name = 'accounts'

urlpatterns = [
] + url(r'^', include('allauth.urls'))