from django.contrib import admin
from django.contrib.gis import admin
from .models import UsersData,RentHome,Transactions,Contract, street,locator

# Register your models here.
admin.site.register(UsersData)

@admin.register(RentHome)
class RentHomeAdmin(admin.OSMGeoAdmin):
    list_display=('')
    search_fields=('')
    filter_fields =('')
    

admin.site.register(Transactions)


admin.site.register(Contract)


@admin.register(locator)
class locatorAdmin(admin.OSMGeoAdmin):
    pass


@admin.register(street)
class streetAdmin(admin.OSMGeoAdmin):
    pass