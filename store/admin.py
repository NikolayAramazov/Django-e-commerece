from django.contrib import admin
from storage.models import Product
from store.models import Ad


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'link')


admin.site.register(Product)
admin.site.register(Ad)