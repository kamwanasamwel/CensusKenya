from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import General, Homes, Homested, nyeri

# admin.site.register()
@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'religion')
    list_filter = ('tribe_or_nationality',)


@admin.register(Homes)
class HomesAdmin(admin.ModelAdmin):
    list_display = ('hs_code', 'hm_code', 'hs_code')


@admin.register(Homested)
class HomestedAdmin(LeafletGeoAdmin):
    list_display = ('hs_code',)



@admin.register(nyeri)
class nyeriAdmin(LeafletGeoAdmin):
    list_display = ('name','const_code', )
# @admin.register(General) is equivalent to
# admin.site.register(General, GeneralAdmin)
# admin.site.register(General, admin.GeneralAdmin)
# admin.site.register(Homes, admin.GeoModelAdmin)
# admin.site.register(Homested, admin.GeoModelAdmin)