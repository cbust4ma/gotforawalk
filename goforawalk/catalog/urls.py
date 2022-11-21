# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:33:05 2022

@author: serdna
"""

from django.urls import re_path as url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eventos/$', views.event, name='event'),
    url(r'^bookmarks/$', views.bookmarks, name='bookmarks'),

]
