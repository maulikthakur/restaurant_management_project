
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Category, MenuItem, Order, OrderItem

# ===== MENU MODELS ADMIN =====

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    list_per_page = 20

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'created_at']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_available', 'price']
    readonly_fields = ['created_at']
    list_per_page = 25
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category')
        }),
        ('Pricing & Availability', {
            'fields': ('price', 'is_available')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

# ===== ORDER MODELS ADMIN =====

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['get_subtotal']
    fields = ['menu_item', 'quantity', 'price', 'special_instructions', 'get_subtotal']
    
    def get_subtotal(self, obj):
        if obj.pk:
            return f"${obj.get_subtotal():.2f}"
        return "$0.00"
    get_subtotal.short_description = 'Subtotal'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'status', 'total_amount', 'get_item_count', 'created_at']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['customer__username', 'customer__email', 'customer__first_name', 'customer__last_name', 'id']
    readonly_fields = ['created_at', 'updated_at', 'calculate_total_display']
    list_editable = ['status']
    list_per_page = 25
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Order Information', {
            'fields': ('customer', 'status', 'total_amount', 'calculate_total_display')
        }),
        ('Customer Details', {
            'fields': ('delivery_address', 'phone_number', 'order_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [OrderItemInline]
    
    actions

