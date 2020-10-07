from io import BytesIO

from django.http import HttpResponse
from django.template.loader import render_to_string
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

from .models import Actividad, Lugar, Isla
from datetime import *

from .serializers import IslaSerializer, ActividadSerializer, LugarSerializer
from .utils import render_to_pdf
from datetime import date
import calendar
class HoraActividadFilter(filters.FilterSet):
    hora_mayor_que = filters.TimeFilter(field_name="hora_inicio", lookup_expr='gte')
    hora_menor_que = filters.TimeFilter(field_name="hora_inicio", lookup_expr='lte')

    class Meta:
        model = Actividad
        fields = ['actividad', 'hora_mayor_que', 'hora_menor_que','lugar']


class ActividadesView(generics.ListAPIView):
    """API View de prueba"""
    queryset = Actividad.objects.filter(dia=calendar.day_name[date.today().weekday()])
    serializer_class = ActividadSerializer
    ordering_fields = ['hora_inicio', ]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_class = HoraActividadFilter


class HoraFilter(filters.FilterSet):
    hora_mayor_que = filters.TimeFilter(field_name="actividad__hora_inicio", lookup_expr='gte')
    hora_menor_que = filters.TimeFilter(field_name="actividad__hora_inicio", lookup_expr='lte')

    class Meta:
        model = Lugar
        fields = ['nombre', 'hora_mayor_que', 'hora_menor_que', ]


class LugaresView(generics.ListAPIView):
    """API View de prueba"""

    queryset = Lugar.objects.all().distinct('id')
    serializer_class = LugarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HoraFilter


class IslaView(viewsets.ModelViewSet):
    queryset = Isla.objects.all()
    serializer_class = IslaSerializer


class LugarView(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

from django.views.generic import View
from datetime import date

class ListEmpleadosPdf(View):

    def get(self, request, *args, **kwargs):
        actividades = Actividad.objects.all().order_by('hora_inicio').values()
        actividadespm = Actividad.objects.all().order_by('hora_inicio').values()
        data = {

            'actividades': actividades
        }
        pdf = render_to_pdf('reporte/actividades.html', data)
        return HttpResponse(pdf, content_type='application/pdf')