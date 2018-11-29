from .models import Perro
from rest_framework import viewsets
from MisPerris.serializers import PerroSerializer

class PerroViewSet( viewsets.ModelViewSet ):
    queryset = Perro.objects.all().order_by( 'nombre' )
    serializer_class = PerroSerializer