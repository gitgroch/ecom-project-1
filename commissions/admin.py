from django.contrib import admin
from .models import Commission
from django_summernote.admin import SummernoteModelAdmin


# Create commissions admin model 
@admin.register(Commission)
class CommissionAdmin(SummernoteModelAdmin):

    list_display = ('full_name', 'email', 'phone_number',)
    search_fields = ['full_name', 'content']
    list_filter = ('full_name',)
    summernote_fields = ('commission_request',)


