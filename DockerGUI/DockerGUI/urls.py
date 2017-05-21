"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from app import views
from django.views.generic import *
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import *
from revproxy.views import ProxyView
from django.contrib.auth.decorators import login_required

#router = routers.DefaultRouter()
#router.register(r'Objet', ObjetViewSet)
#router.register(r'image', image)

from .views import TestProxyView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')) ,
    url(r'^ui/(?P<path>.*)$', login_required(TestProxyView.as_view())),
    url(r'^app/', include('app.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', auth_views.login,{'template_name': 'auth/login.html','redirect_authenticated_user':True   },name='login' ) ,
    #url(r'^api/', include(router.urls)),
    #url(r'^objets/$', Objetlist.as_view()),
    url(r'^ps/$', PsList.as_view()),
    url(r'^build/$', Conteneurs_build.as_view()),
    url(r'^run/$',Conteneurs_run.as_view()) ,
    url(r'^logs/$',Conteneurs_logs.as_view()) ,
    url(r'^pause/$',Conteneurs_pause.as_view()) ,
    url(r'^unpause/$',Conteneurs_unpause.as_view()) ,
    url(r'^rm/$',Conteneurs_rm.as_view()) ,
    url(r'^rename/$',Conteneurs_rename.as_view())  ,
    url(r'^rmstopped/$',Conteneurs_rm_stopped.as_view()) ,
    url(r'^restart/$',Conteneurs_restart.as_view()) ,
    url(r'^start/$',Conteneurs_start.as_view()) ,
    url(r'stats/$',Conteneurs_stats.as_view()) ,
    url(r'stop/$',Conteneurs_stop.as_view()) ,
    url(r'top/$',Conteneurs_top.as_view()) ,
    url(r'history/$',Images_history.as_view()),
    url(r'images/$',Images_images.as_view()) ,
    url(r'pull/$',Images_pull.as_view()) ,
    url(r'remove/$',Images_remove_image.as_view()) ,
    url(r'search/$',Images_search.as_view()) ,
    url(r'tag/$',Images_tag.as_view()) ,
    url(r'^session/$', sess,)
]
