from django.contrib import admin

from .models import Lead


class LeadAdmin(admin.ModelAdmin):
    list_display = ('lead_type', 'name', 'email',
                    'contact_date', 'phone', 'message', 'is_hot', 'is_warm', 'is_cold')
    list_display_links = ('name', 'lead_type',)
    search_fields = ('name', 'email', )
    list_per_page = 25


admin.site.register(Lead, LeadAdmin)
