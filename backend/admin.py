from django.contrib import admin
from . models import *

# Register your models here.
class ChambreHotelAdmin(admin.ModelAdmin):
    list_display = ('numeroChambre', 'type', 'prix', 'petit_dejeuner', 'etage', 'description', 'disponibilite')

admin.site.register(ChambreHotel, ChambreHotelAdmin)