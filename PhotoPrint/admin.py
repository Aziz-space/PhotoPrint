from django.contrib import admin
from .models import Service, SI, Status, Order, OI

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')

class SIAdmin(admin.ModelAdmin):
    list_display = ('width', 'height', 'service') 
    list_filter = ('service',)
    search_fields = ('width', 'height')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'service', 'client_data')
    list_filter = ('status',)

@admin.register(OI)
class OIAdmin(admin.ModelAdmin):
    list_display = ('order', 'service_item', 'quantity')
    list_filter = ('order', 'service_item')
    search_fields = ('order__id', 'service_item__width', 'service_item__height')


admin.site.register(Service, ServiceAdmin)
admin.site.register(SI, SIAdmin)
