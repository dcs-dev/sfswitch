from django.conf.urls import  include, url ## , patterns
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from enable_disable import views

admin.autodiscover() 

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    re_path(r'oauth_response?$', views.oauth_response, name='oauth_response'),
    path('logout', views.logout, name='logout'),
    re_path(r'^loading/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.loading),
    re_path(r'^job_status/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.job_status),
    re_path(r'^job/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.job),
    re_path(r'^update_metadata/(?P<job_id>[0-9A-Za-z_\-]+)/(?P<metadata_type>[0-9A-Za-z_\-]+)/$', views.update_metadata),
    re_path(r'^check_deploy_status/(?P<deploy_job_id>\d+)/$', views.check_deploy_status),
    re_path(r'^auth_details/$', views.auth_details),
]

# urlpatterns = patterns('',
#     url(r'^$', 'enable_disable.views.index', name='index'),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^oauth_response/$', 'enable_disable.views.oauth_response', name='oauth_response'),
#     url(r'^logout/$', 'enable_disable.views.logout', name='logout'),
#     url(r'^loading/(?P<job_id>[0-9A-Za-z_\-]+)/$', 'enable_disable.views.loading'),
#     url(r'^job_status/(?P<job_id>[0-9A-Za-z_\-]+)/$', 'enable_disable.views.job_status'),
#     url(r'^job/(?P<job_id>[0-9A-Za-z_\-]+)/$', 'enable_disable.views.job'),
#     url(r'^update_metadata/(?P<job_id>[0-9A-Za-z_\-]+)/(?P<metadata_type>[0-9A-Za-z_\-]+)/$', 'enable_disable.views.update_metadata'),
#     url(r'^check_deploy_status/(?P<deploy_job_id>\d+)/$', 'enable_disable.views.check_deploy_status'),
#     url(r'^auth_details/$', 'enable_disable.views.auth_details'),
# )
