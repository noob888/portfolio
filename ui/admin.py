from django.contrib import admin
from .models import ContactModel, HomeContactModel

@admin.register(ContactModel)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'message']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(HomeContactModel)
class HomePageEmailAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']


