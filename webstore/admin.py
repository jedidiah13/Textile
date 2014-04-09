from django.contrib import admin
from webstore.models import StoreCategory, StoreItem

class StoreAdmin(admin.ModelAdmin):
	pass
# Register your models here.
admin.site.register(StoreItem, StoreAdmin)
admin.site.register(StoreCategory, StoreAdmin)
