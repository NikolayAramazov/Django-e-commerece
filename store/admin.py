from django.contrib import admin
from storage.models import Product, ProductImage
from store.models import Ad


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    inlines = [ProductImageInline]


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'link')


admin.site.register(Product, ProductAdmin)
admin.site.register(Ad, AdAdmin)