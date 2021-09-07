from django.contrib import admin
from django.utils.html import mark_safe
from . import models


# @admin.register(models.RoomType)
# class ItemAdmin(admin.ModelAdmin):
#     pass
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")}
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (
            "Space",
            {"fields": ("guests", "beds", "bedrooms", "baths")}
        ),
        (
            "More about the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rule")
            }
        ),
        (
            "Last Details",
            {"fields": ("host",)}
        )
        
    )

    list_display = ("name", "country", "city", "price", "address", "beds", "bedrooms", "baths", "guests", "check_in", "check_out", "instant_book", "host", "count_amenities", "count_photos", "total_ratings")

    list_filter = ("host__superhost", "instant_book", "city", "country")

    raw_id_fields = ("host",)

    search_fields = ["city", "^host__username"]

    filter_horizontal = ('amenities', 'facilities', 'house_rule')

    ordering = ('beds', 'price')

    readonly_fields = ('check_out', 'check_in')

    # def save_model(self, request, obj, form, change):
    #     # obj.user = request.user
      
    #     super().save_model(request, obj, form, change)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
