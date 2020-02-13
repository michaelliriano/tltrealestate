from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'email', 'hire_date')
    list_display_links = ('id', 'name', 'title')
    search_fields = ('name',)
    list_per_page = 5


admin.site.register(Realtor, RealtorAdmin)
