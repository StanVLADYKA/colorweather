from django.contrib import admin
from .models import Days

admin.site.register(Days)

class DaysAdmin(admin.ModelAdmin):
    list_display = ('date', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7')

# Register your models here.
