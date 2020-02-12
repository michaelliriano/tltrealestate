from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'active', 'sold',
                    'price', 'city', 'state', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('city', 'price')
    list_editable = ('active', 'sold')
    search_fields = ('title', 'description', 'address',
                     'city', 'zipcode', 'price')
    list_per_page = 5


admin.site.register(Listing, ListingAdmin)
