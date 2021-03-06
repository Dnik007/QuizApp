"""quizapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
#    url(r'',include('quiz.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^$', views.role, name='role'),
    url(r'^participantRegistration/$', views.participantRegistration, name='participantRegistration'),
    url(r'^masterRegistration/$', views.masterRegistration, name='masterRegistration'),
    url(r'^participantLogin/$',auth_views.login ,{ template_name='registration/participantlogin.html'}, name='participantLogin'),
    url(r'^masterLogin/$',auth_views.login ,{ template_name='registration/masterlogin.html'}, name='masterLogin'),
    url(r'^logout/$',auth_views.logout,{ template_name='registration/logout.html'}, name='logout')
]
