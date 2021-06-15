from django.contrib import admin
import nested_admin
from .models import Schedule

class ScheduleAdmin(nested_admin.NestedModelAdmin):
    search_fields=('barber','date','time','name')
    fields =('cpf','email','barber','date','time','name')

admin.site.register(Schedule,ScheduleAdmin)