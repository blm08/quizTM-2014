from django.conf.urls import patterns, url

from quiz.views import *

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^create/$', create, name="create"),
    url(r'^(\d+)/complete/', complete, name="complete"),
    url(r'^find/', find, name="find"),
    url(r'^findquiz/', findquiz, name="findquiz"),
    url(r'^savedraft/', savedraft, name="savedraft"),
    url(r'^listdrafts/', listdrafts, name="listdrafts"),
    url(r'^getdraft/', getdraft, name="getdraft"),
)