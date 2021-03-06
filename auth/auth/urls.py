"""auth URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from authentication.views import index, registration, base, user_login, user_logout, success, dashboard, cookiee, send_email

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', base),
    url(r'^registration/$', registration),
    url(r'^index/$', index),
    url(r'^login/$', user_login),
    url(r'^logout/$', user_logout),
    url(r'^success/$', success),
    url(r'^dashboard/$', dashboard),
    url(r'^cookiee/$', cookiee),
    url(r'^email/$', send_email),
]
