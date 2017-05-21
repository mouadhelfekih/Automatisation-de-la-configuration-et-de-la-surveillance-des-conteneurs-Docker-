from django.conf.urls import *
from django.views.generic import *
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url




urlpatterns = [
      url(r'^inscription$', views.inscription, name='inscription'),
     url(r'^profile', views.profile,name="profile"),
     url(r'^logout/$', views.logout,)
]
