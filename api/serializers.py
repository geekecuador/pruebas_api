from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from rest_framework import serializers
from .models import Actividad,Isla, Lugar



class IslaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isla
        fields = ('id','nombre',)





class LugarSerializer(serializers.ModelSerializer):

    isla = IslaSerializer()

    class Meta:
        model = Lugar
        fields = ('id','nombre', 'isla', )



class ActividadSerializer(serializers.ModelSerializer):

    lugar  = LugarSerializer()
    class Meta:
        model = Actividad
        fields = ('actividad','hora_inicio','hora_fin','dia','lugar')









