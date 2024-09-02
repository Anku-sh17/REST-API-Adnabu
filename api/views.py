from rest_framework import generics, permissions
from .models import Product, Variant, Collection, Category
from .serializers import ProductSerializer, VariantSerializer, CollectionSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class VariantListView(generics.ListAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    permission_classes = [permissions.IsAuthenticated]

class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductsByCollectionView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        collection_ids = self.request.query_params.getlist('collection_id')
        return Product.objects.filter(collections__id__in=collection_ids)

class VariantsByCollectionView(generics.ListAPIView):
    serializer_class = VariantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        collection_ids = self.request.query_params.getlist('collection_id')
        return Variant.objects.filter(product__collections__id__in=collection_ids)

class VariantsByCategoryView(generics.ListAPIView):
    serializer_class = VariantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        return Variant.objects.filter(product__categories__id=category_id)
