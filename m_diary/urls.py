from django.conf.urls import url

from m_diary.views import diary_index

urlpatterns = [
    url(r'^$', diary_index),
]
