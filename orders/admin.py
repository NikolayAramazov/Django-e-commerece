from django.contrib import admin

from orders.models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    ...


admin.site.register(Order)
