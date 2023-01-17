# -*- coding: utf-8 -*-

from django.conf.urls import url

import iron_piece.views as i_v


urlpatterns = [
    url(r'^$', i_v.iron_piece),
]
