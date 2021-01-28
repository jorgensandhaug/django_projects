from django.db import models
from tastypie import resources
from tastypie.resources import ModelResource
from blogs.models import Blogpost

class BlogpostResource(ModelResource):
    class Meta:
        queryset = Blogpost.objects.all()
        resource_name = 'blogposts'
