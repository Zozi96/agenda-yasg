from django.contrib import admin
from .models import Contact, Group


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'email',
        'group'
    )
    list_filter = (
        'group',
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
