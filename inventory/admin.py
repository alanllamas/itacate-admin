from django.contrib import admin

from inventory import models

# Register your models here.
@admin.register(models.Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'categories', 'created', 'modified']
  search_fields = ['name']

@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'created', 'modified']
  search_fields = ['name']


@admin.register(models.Product_Category)
class Product_CategoryModelAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'created', 'modified']
  search_fields = ['name']


@admin.register(models.Warehouse)
class WarehouseModelAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'created', 'modified']
  search_fields = ['name']


@admin.register(models.Inventory)
class InventoryModelAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'created', 'modified']
  search_fields = ['name']





