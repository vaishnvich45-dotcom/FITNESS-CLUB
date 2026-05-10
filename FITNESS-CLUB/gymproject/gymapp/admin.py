from django.contrib import admin
from .models import FitnessData

@admin.register(FitnessData)
class FitnessDataAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'weight',
        'height',
        'bmi',
        'category',
        'stress_level'
    )
    list_filter = ('category', 'stress_level')
    search_fields = ('name',)