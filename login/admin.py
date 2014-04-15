from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from login.models import UserProfile, OrderItem, Order
# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)       

class OrderAdmin(admin.ModelAdmin):
	pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderAdmin)
