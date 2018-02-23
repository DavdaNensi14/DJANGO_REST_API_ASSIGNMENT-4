from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ipl_schedule import settings
from api.views import *
from rest_framework.authtoken import views as tokenView

urlpatterns = patterns('',
    url(r'^login/', tokenView.obtain_auth_token),
    url(r'^register/$', user_Register, name='user_Register'),
    url(r'^team/add/$', team_create, name='team_create'),
    url(r'^team/list/$', team_list, name='team_list'),
    url(r'^team/details/(?P<pk>[0-9]+)/$', team_details, name='team_details'),
    url(r'^team/update/(?P<pk>[0-9]+)/$', team_update, name='team_update'),
    url(r'^team/delete/(?P<pk>[0-9]+)/$', team_delete, name='team_delete'),
    url(r'^venue/add/$', venue_create, name='venue_create'),
    url(r'^venue/list/$', venue_list, name='team_list'),
    url(r'^venue/details/(?P<pk>[0-9]+)/$', venue_details, name='venu_details'),
    url(r'^venue/update/(?P<pk>[0-9]+)/$', venue_update, name='venu_update'),
    url(r'^venue/delete/(?P<pk>[0-9]+)/$', venue_delete, name='venu_delete'),
    url(r'^match/add/$', match_create, name='match_create'),
    url(r'^match/list/$', match_list, name='team_list'),
    url(r'^match/details/(?P<pk>[0-9]+)/$', match_details, name='match_details'),
    url(r'^match/update/(?P<pk>[0-9]+)/$', match_update, name='match_update'),
    url(r'^match/delete/(?P<pk>[0-9]+)/$', match_delete, name='match_delete'),
    url(r'^fav/list/$', fav_list, name='fav_list'),
    url(r'^fav/add/$', fav_add, name='fav_add'),
    url(r'^fav/update/(?P<pk>[0-9]+)/$', fav_update, name='fav_update'),
    url(r'^fav/details/(?P<pk>[0-9]+)/$', fav_details, name='fav_details'),
    url(r'^fav/delete/(?P<pk>[0-9]+)/$', fav_delete, name='fav_details'),
    # url(r'^venue/search/$', venue_search, name='venu_search'),
    url(r'^match/today/$', match_today, name='match_today'),
    url(r'^match/nextweek/$', match_nextweek, name='match_nextweek'),
    
)
