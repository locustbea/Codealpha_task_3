from django.contrib import admin
from .models import MenuItem, Table, InventoryItem, Order

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(InventoryItem)
admin.site.register(Order)
