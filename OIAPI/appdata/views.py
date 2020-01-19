from django.shortcuts import render
from rest_framework import generics
from .models import Appdata,Refined
from django_filters import rest_framework
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
from .filters import appdatafilter
from .serializers import AppdataSerializer,RefinedSerializer
from rest_framework.generics import ListAPIView
from  rest_framework.filters import SearchFilter
from django_filters import rest_framework
"""
class appdata(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  "name"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filter']=appdatafilter(self.request.GET,queryset=self.get_queryset())
        return context

"""
"""it works ...somewhat
class appdataAPIview(generics.ListCreateAPIView):
    search_fields = {'name', 
                     'created'
                     }
    filter_backends = (SearchFilter,)
    queryset = Appdata.objects.all()
    serializer_class = AppdataSerializer
"""
class appfilter(rest_framework.FilterSet):
    min_created=rest_framework.DateTimeFilter(field_name="created",lookup_expr="gte",)
    max_created = rest_framework.DateTimeFilter(field_name="created", lookup_expr="lte")
    class Meta:
        model = Appdata
        fields=['name','min_created','max_created']


class appdataAPIview(generics.ListAPIView):

    filter_backends = (rest_framework.DjangoFilterBackend,)
    queryset = Appdata.objects.all()
    serializer_class = AppdataSerializer
    filterset_class = appfilter

class reffilter(rest_framework.FilterSet):
    min_created=rest_framework.DateTimeFilter(field_name="created",lookup_expr="gte",)
    max_created = rest_framework.DateTimeFilter(field_name="created", lookup_expr="lte")
    class Meta:
        model = Refined
        fields=['name','min_created','max_created']


class refinedAPIview(generics.ListAPIView):

    filter_backends = (rest_framework.DjangoFilterBackend,)
    queryset = Refined.objects.all()
    serializer_class = RefinedSerializer
    filterset_class = reffilter