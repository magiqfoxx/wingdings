from django.conf.urls import include, url
from django.contrib import admin

from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wingdings.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^admin/', include(admin.site.urls)),
]
