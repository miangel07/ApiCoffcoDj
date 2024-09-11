from django.urls import path,include
from apps.finca.api.Views import FincaViewset
from rest_framework import routers
routerFinca = routers.DefaultRouter()
routerFinca.register(prefix='finca',basename='finca',viewset=FincaViewset)