from django.contrib import admin
from interview.inventory.models import (
    Inventory,
    InventoryLanguage,
    InventoryTag,
    InventoryType,
)
# Register your models here.

admin.site.register(Inventory)
admin.site.register(InventoryLanguage)
admin.site.register(InventoryTag)
admin.site.register(InventoryType)
