from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User admin"""
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthday",
                    "language",
                    "currency",
                    "superhost"
                )
            }
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "is_staff",
        "is_superuser",
        'superhost',
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

# register is to be able to see your model in the admin panel
# @admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
#     """ Custom User admin"""

    # list_display = ('username', 'gender', 'language', 'currency', 'superhost')

    list_filter = ('currency', 'language', 'superhost',)

    readonly_fields = ('last_login', 'date_joined')


# admin.site.register(models.User, CustomUserAdmin)
