from rest_framework import viewsets
from apps.rol.models import RolModels
from apps.rol.api.Serializers import RolSerializers


class rolViewSet(viewsets.ModelViewSet):
    serializer_class=RolSerializers
    queryset=RolModels.objects.all()