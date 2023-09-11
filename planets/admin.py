from django.contrib import admin
from .models import Planet

class PlanetAdmin(admin.ModelAdmin):
  list_display = ('name', 'id', 'mass', 'number_of_moons', 'is_gas_giant')

admin.site.register(Planet, PlanetAdmin)
