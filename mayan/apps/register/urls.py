from __future__ import unicode_literals

from django.conf.urls import url

from .views import RegisterListView

urlpatterns = [
    url(r'^list/$', RegisterListView.as_view(), name='register_list'),
    #url(
    #    r'^(?P<pk>\d+)/register/out/$', CheckoutDocumentView.as_view(),
    #    name='checkout_document'
    #),
    #url(
    #    r'^(?P<pk>\d+)/register/in/$', DocumentCheckinView.as_view(),
    #    name='checkin_document'
    #),
    #url(
    #    r'^(?P<pk>\d+)/register/info/$', CheckoutDetailView.as_view(),
    #    name='checkout_info'
    #),
]
