from .models import Perro
from .models import User
from rest_framework import serializers


class PerroSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Perro
        fields = ( 'id','nombre', 'raza', 'caracteristica', 'estado', 'imageUrl' )



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'admin')
