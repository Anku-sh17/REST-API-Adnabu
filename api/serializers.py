from rest_framework import serializers
from .models import Product, Variant, Image, Collection, Category

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['source', 'alt_text', 'updated_at']

class VariantSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Variant
        fields = ['title', 'created_at', 'updated_at', 'available_for_sale', 'price', 'image']

    def get_title(self, obj):
        return f"{obj.product.title} - {obj.title}"

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'created_at', 'updated_at', 'images']

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['title', 'published', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'created_at', 'updated_at']
