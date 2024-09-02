from django.contrib import admin
from .models import Product, Variant, Image, Collection, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'available_for_sale', 'price', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('available_for_sale', 'created_at', 'updated_at')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'source', 'updated_at', 'product')
    search_fields = ('alt_text',)
    list_filter = ('updated_at',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'updated_at')
    search_fields = ('title',)
    list_filter = ('published', 'updated_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
