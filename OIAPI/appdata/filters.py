import django_filters

from .models import Appdata


class appdatafilter(django_filters.FilterSet):
    class Meta:
        model= Appdata
        fields = {
            'name': ['icontains']
        }