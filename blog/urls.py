# from django.conf.urls import url
# from . import views


# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
# ]

from django.conf.urls import patterns, include, url
from blog.views import *
from . import views

 
urlpatterns = patterns('',
	url(r'^$', views.post_list, name='post_list'),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
)