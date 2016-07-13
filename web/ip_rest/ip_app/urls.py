from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ip/$', views.ip_list),
]
