from django.contrib import admin
from webstore.models import StoreCategory, StoreItem, Order, OrderItem



class OrderAdmin(admin.ModelAdmin):
	pass


class StoreAdmin(admin.ModelAdmin):
	pass
# Register your models here.
admin.site.register(StoreItem, StoreAdmin)
admin.site.register(StoreCategory, StoreAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderAdmin)