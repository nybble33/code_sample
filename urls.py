"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

import cms.auth as cms_auth
# ~from cms.auth import nybble_user_login, nybble_user_logout, ajax_login, ajax_logout
#~ from nbot.views import n_bot_sign

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

prefix = ''

urlpatterns = [
    url(r'^logout/$', cms_auth.nybble_user_logout),
    url(r'^login/$', cms_auth.nybble_user_login),
    url(r'^ajax_login/$', cms_auth.ajax_login),
    url(r'^ajax_logout/$', cms_auth.ajax_logout),
    path(prefix+'admin/', admin.site.urls),
    url(prefix+'', include('cms.urls')),
    url(prefix+'tools/', include('tools.urls')),
    url(prefix+'m_diary', include('m_diary.urls')),
    url(prefix+'m_design/', include('m_design.urls')),
    url(prefix+'anki', include('anki.urls')),
    url('nbot/', include('nbot.urls')),
    url('iron_piece', include('iron_piece.urls')),
]
