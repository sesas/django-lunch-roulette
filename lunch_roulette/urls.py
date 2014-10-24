from django.conf.urls import patterns, url, include

from . import views

urlpatterns = patterns('',
    # url(r'^(?P<name>[\w-]+)$', LunchView.as_view()),
    url(r'^join/$', views.join, name='lunch_join'),
    url(r'^roll/$', views.roll, name='lunch_roll'),
)