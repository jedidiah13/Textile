from django.contrib import admin
from login.models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
	pass

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderAdmin)
