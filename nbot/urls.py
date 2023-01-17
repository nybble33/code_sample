from django.conf.urls import url

# import views here
# from nbot.views import webhook
import nbot.views as n_v

urlpatterns = [
    # url(r'^$', screen_width),
    # url(r'^tinymce/$', tiny_mce),
    url(r'^1842197193/$', n_v.webhook),
]
