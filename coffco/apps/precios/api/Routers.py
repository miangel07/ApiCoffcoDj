from django.urls import path,include
from apps.precios.api.Views import PreciosViewSet
from rest_framework import routers
routerPrecios = routers.DefaultRouter()
routerPrecios.register(prefix='precios',basename='precios',viewset=PreciosViewSet)