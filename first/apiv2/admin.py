from django.contrib import admin

# Register your models here.

from api_class.models import Item

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ("__all__")

admin.site.register(Item)