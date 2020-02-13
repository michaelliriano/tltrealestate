from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'sold',
                    'price', 'city', 'state', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('city', 'price')
    list_editable = ('is_published', 'sold')
    search_fields = ('title', 'description', 'address',
                     'city', 'zipcode', 'price')
    list_per_page = 5


admin.site.register(Listing, ListingAdmin)
