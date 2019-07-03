import datetime
from dateutil.relativedelta import relativedelta
import django_filters
from django_filters import rest_framework as filters

from blog import models


class BlogFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Entry
        fields = ['name']


class UserFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Entry
        fields = ['name']


class EntryFilter(filters.FilterSet):
    headline = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Entry
        fields = ['headline']

