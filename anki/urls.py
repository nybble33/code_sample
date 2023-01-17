# -*- coding: utf-8 -*-

from django.conf.urls import url

import anki.views as a_w


urlpatterns = [
    url(r'^$', a_w.card_index),
    url(r'^/get_card/$', a_w.card_detail),
    url(r'^/remove_card/$', a_w.card_remove),
]