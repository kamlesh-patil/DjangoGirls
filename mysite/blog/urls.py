from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'abc/$', views.get_list, name='get_list'),
]
