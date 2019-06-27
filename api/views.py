from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from . import serializers
from blog import models as blog_models
from . import filters


class BlogViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = blog_models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    filter_class = filters.BlogFilter


class UserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = blog_models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_class = filters.UserFilter


class EntryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = blog_models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer
