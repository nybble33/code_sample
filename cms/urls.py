# -*- coding: utf-8 -*-

from django.conf.urls import url

from cms.views import index, pages, page_detail, send_mail
from cms.views import hidden_page_detail, rebus, vk_friends
from cms.views import new_tpl, iron_piece

urlpatterns = [
    url(r'^$', index),
    url(r'^tpl/$', new_tpl),
    url(r'^pages/$', pages),
    url(r'^page/(?P<page_slug>[-\w]+)/$', page_detail),
    url(r'^secret_page/(?P<page_slug>[-\w]+)/$', hidden_page_detail),
    url(r'^mail', send_mail),
    url(r'^rebus', rebus),
    url(r'^vk_friends', vk_friends),
    # ~url(r'^iron_piece', iron_piece),
]
