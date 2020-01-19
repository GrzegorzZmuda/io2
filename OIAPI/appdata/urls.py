from rest_framework import routers
from .api import AppdataViewSet,RefinedViewSet
from django.urls import path
from . import views
router = routers.DefaultRouter()
router.register('api/appdata',AppdataViewSet,'appdata')
router.register('api/refined',RefinedViewSet,'appdata')

urlpatterns =[
    path('appdata/',views.appdataAPIview.as_view()),
    path('refined/',views.refinedAPIview.as_view())
]

urlpatterns +=router.urls