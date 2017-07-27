from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^home$',views.home),
    url(r'^sign_up$',views.sign_up),
    url(r'^add_item$',views.add_item),
    url(r'^delete_item$',views.delete_item),
    url(r'^log_out$',views.log_out),
    url(r'^add_to_wish$',views.add_to_wish),
    url(r'^remove_list_item$',views.remove_list_item),
    url(r'^wishers/(?P<word>\w+)$',views.wishers),
]