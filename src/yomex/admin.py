from django.contrib import admin

from .models import Perfume,WristWatch,Glass,Shoes



admin.site.site_header = 'Yomex admin'


class GlassAdmin(admin.ModelAdmin):
    list_display                = ('name','description','discount','price','date_uploaded')
    search_fields               = ('name',)
    readonly_fields             = ('date_uploaded',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Glass,GlassAdmin)


admin.site.register(Perfume)
admin.site.register(WristWatch)

admin.site.register(Shoes)
# Register your models here.


