from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from admin_dashboard.views import tlistView,adminD,tlistUpdate,plistView,plistUpdate

app_name = 'adminD'

urlpatterns = [
    path('',adminD, name='admin_D'),
    path('tour-listview',tlistView.as_view(),name='tour_list'),
    url(r'^updateT/(?P<pk>\d+)/$',tlistUpdate.as_view(), name='update'),
    path('plist-view',plistView.as_view(),name='player_list'),
    url(r'^updateP/(?P<pk>\d+)/$',plistUpdate.as_view(), name='updatep'),
]
