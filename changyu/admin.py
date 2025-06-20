from django.contrib import admin

# Register your models here.
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender', 'email', 'contacted', 'contact_note', 'created_at')
    list_filter = ('category', 'gender', 'created_at', 'contacted')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
