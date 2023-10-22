from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import RealEstate, Category, Photo, TimeSlot, Booking, Contracts


# Register your models here.
class RealEstateAdmin(admin.ModelAdmin):
    list_display = ['id', 'district', 'address', 'area', 'floor', 'rooms', 'category']
    list_display_links = ['id', 'district', 'address', 'area', 'floor', 'rooms', 'category']
    list_filter = ['category','district', 'address', 'area', 'floor', 'rooms', 'type', 'layout', 'finishing', 'bathroom',
                   'balcony', 'animals', 'children', 'parking']
    ordering = ['-pk']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100px">')
        else:
            return '-'

    get_photo.short_description = 'Фото'


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'real_estate', 'get_photo']
    list_display_links = ['id', 'real_estate', 'get_photo']

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px">')
        else:
            return '-'

    get_photo.short_description = 'Фото'



class BookingAdmin(admin.ModelAdmin):
    list_display = ['object', 'time_slot', 'client_name', 'realtor']
    list_display_links = ['object', 'time_slot', 'client_name', 'realtor']




admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Category)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Contracts)

admin.site.site_title = 'Управление сервисом'
admin.site.site_header = 'Управление сервисом'
