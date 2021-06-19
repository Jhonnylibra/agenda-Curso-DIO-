from django.contrib import admin
from core.models import Evento
# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'titulo', 'data_evento')
admin.site.register(Evento, EventoAdmin)
