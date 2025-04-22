from django.contrib import admin
from storage.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


admin.site.register(Product)
