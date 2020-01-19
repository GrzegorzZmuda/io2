from .models import Appdata,Refined
from rest_framework import viewsets, permissions
from .serializers import AppdataSerializer,RefinedSerializer

class AppdataViewSet(viewsets.ModelViewSet):
    queryset = Appdata.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppdataSerializer

class RefinedViewSet(viewsets.ModelViewSet):
    queryset = Refined.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RefinedSerializer