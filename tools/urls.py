from django.conf.urls import url

from tools.views import screen_width, tiny_mce, canvas01, dragNdrop

urlpatterns = [
    url(r'^$', screen_width),
    url(r'^tinymce/$', tiny_mce),
    url(r'^canvas01/$', canvas01),
    url(r'^dndrop/$', dragNdrop),
]
