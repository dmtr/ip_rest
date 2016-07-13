from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ip/$', views.IpList.as_view(), name='ip-list'),
]
