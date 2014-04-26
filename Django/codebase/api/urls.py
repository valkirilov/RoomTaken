from django.conf.urls import patterns, include, url

from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from api.models import Snippet
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group
    
class SnippetsViewSet(viewsets.ModelViewSet):
    model = Snippet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetsViewSet)
#router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)