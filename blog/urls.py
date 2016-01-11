# from django.conf.urls import url
# from . import views


# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
# ]

from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
	url(r'^$', views.post_list, name='post_list'),
    # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^user/logout/$', views.logout_page, name='logout'),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^accounts/login/$', views.custom_login, name='login'),
    url(r'^user/register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^user/home/$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^user/blog/$', views.post, name='post'),
    url(r'^user/blog/post/$', views.user_post, name='user_post'),
    url(r'^user/blog/post/add/$', views.blog_post, name='blog_post')
)