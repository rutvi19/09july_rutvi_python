from django.contrib import admin
from .models import Doctor, Specialization


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'specialization',
        'hospital',
        'city',
        'experience',
        'available'
    )
    list_filter = ('specialization', 'city', 'available')
    search_fields = ('name', 'hospital', 'city')
    list_editable = ('available',)
    ordering = ('name',)
    list_per_page = 10


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
