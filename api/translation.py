from modeltranslation.translator import register, TranslationOptions
from .models import Actividad, Isla,Lugar


@register(Actividad)
class ActividadTranslationOptions(TranslationOptions):
    fields = ('actividad',)

@register(Isla)
class IslaTranslationOptions(TranslationOptions):
    fields = ('nombre',)

@register(Lugar)
class IslaTranslationOptions(TranslationOptions):
    fields = ('nombre',)