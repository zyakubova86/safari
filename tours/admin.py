from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'is_active', 'created_at')
    ordering = ('-created_at',)

class TourProgramInline(admin.StackedInline):
    model = TourProgram
    extra = 0

class TourGalleryImageInline(admin.TabularInline):
    model = TourGalleryImage
    extra = 0

class ToursAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'tour_category', 'itinerary', 'is_active', 'created_at')
    ordering = ('-created_at',)
    # prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('slug',)
    inlines = [TourProgramInline, TourGalleryImageInline]


    def image_tag(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit: cover;" />'.format(obj.main_image.url))
        return '-'
    image_tag.short_description = 'Image'


class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'created_at')
    ordering = ('-created_at',) 
    prepopulated_fields = {"slug": ("name",)}


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit: cover;" />'.format(obj.image.url))
        return '-'
    image_tag.short_description = 'Image'


class TourBookingAdmin(admin.ModelAdmin):   
    list_display = ('tour', 'email', 'guest_number', 'arrival_date', 'status', 'created_at')
    ordering = ('-created_at',)


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'email', 'phone', 'created_at')
    ordering = ('-created_at',)

class UzbekistanAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    ordering = ('-created_at',)

class UzbekistanCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    ordering = ('-created_at',)


class UzbekistanCitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Slider, SliderAdmin)
admin.site.register(Tours, ToursAdmin)
admin.site.register(TourCategory, TourCategoryAdmin)
admin.site.register(TourBooking, TourBookingAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(Uzbekistan, UzbekistanAdmin)
admin.site.register(UzbekistanCategory, UzbekistanCategoryAdmin)
admin.site.register(UzbekistanCities, UzbekistanCitiesAdmin)
    
