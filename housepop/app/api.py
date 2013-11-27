# app/api.py
#from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from app.models import Post

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['is_staff', 'is_superuser']

class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
#        authorization = Authorization()

