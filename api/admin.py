from django.contrib import admin
from .models import Actividad,Lugar, Isla
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.contrib.admin import SimpleListFilter

# Register your models here.
from modeltranslation.admin import TranslationAdmin
class LugarAdmin(TranslationAdmin):
    list_display = ('nombre','isla')
    search_fields = ('nombre','isla__nombre',)


admin.site.register(Lugar, LugarAdmin)




class TipoDia(SimpleListFilter):
    # Strings to display as a header in filter
    title = 'Parte del día'
    parameter_name = 'parte_dia'

    # return a tuple of desired fields of a model
    def lookups(self, request, model_admin):
        return (
            ('manana', 'Mañana'),
            ('tarde', 'Tarde'),

        )

    # Queryset for each field to render in change_list template
    def queryset(self, request, queryset):
        if self.value() == 'manana':
            return queryset.filter(hora_inicio__lte='12:00')
        if self.value() == 'tarde':
            return queryset.filter(hora_inicio__gte='12:00')


class ActividadAdmin(TranslationAdmin):

    raw_id_fields = ('lugar',)
    list_display = ('dia','hora_inicio','lugar', 'actividad_es','actividad_en',)
    list_filter = ('dia',TipoDia,'lugar__isla',)
    #autocomplete_fields = ('lugar',)


admin.site.register(Actividad, ActividadAdmin)

class IslaAdmin(TranslationAdmin):
    pass
admin.site.register(Isla, TranslationAdmin)