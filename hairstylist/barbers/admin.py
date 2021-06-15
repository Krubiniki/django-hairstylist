from django.contrib import admin
import nested_admin
from .models import Barber

class BarberAdmin(nested_admin.NestedModelAdmin):
    search_fields=('email','name')
    fields =('user','email','name')

admin.site.register(Barber,BarberAdmin)