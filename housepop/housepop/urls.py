from django.conf.urls import patterns, include, url
from tastypie.api import Api
from app.api import PostResource, UserResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())

#post_resource = PostResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'housepop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'api/', include(post_resource.urls)),

    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
