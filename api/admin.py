from django.contrib import admin
from django.utils.html import format_html

from djaa_list_filter.admin import (
    AjaxAutocompleteListFilterModelAdmin,
)

# Register your models here.
from .models import (
    Mesa,Categoria,Plato
)

admin.site.register(Mesa)
admin.site.register(Categoria)

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    
    def imagen_html(self,obj):
        return format_html('<a href="{}" target="_blank"><img src="{}" width=100px /></a>'.format(obj.plato_img.url,obj.plato_img.url))
    
    list_display = ('plato_nom','categoria_id','imagen_html','plato_pre')
    list_editable = ('plato_pre',)
    list_filter = ('categoria_id',)
    #autocomplete_list_filter = ('categoria_id',)
    
    