# -*- coding: utf-8 -*-

from m_design.views import index, starter, parallax, sieve_era,\
     binary_mouse, conway_gol

from django.conf.urls import url

urlpatterns = [
    url(r'^$', index),
    url(r'starter/$', starter),
    url(r'parallax/$', parallax),
    url(r'sieve_era/$', sieve_era),
    url(r'bin_mouse/$', binary_mouse),
    url(r'conway_gol/$', conway_gol),
]
