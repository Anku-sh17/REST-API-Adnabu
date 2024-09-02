from django.urls import path
from .views import (
    ProductListView, VariantListView, CollectionListView,
    ProductsByCollectionView, VariantsByCollectionView, VariantsByCategoryView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('variants/', VariantListView.as_view(), name='variant-list'),
    path('collections/', CollectionListView.as_view(), name='collection-list'),
    path('products/by-collection/', ProductsByCollectionView.as_view(), name='products-by-collection'),
    path('variants/by-collection/', VariantsByCollectionView.as_view(), name='variants-by-collection'),
    path('variants/by-category/', VariantsByCategoryView.as_view(), name='variants-by-category'),
#     path('collections/<int:collection_id>/products/', ProductsByCollectionView.as_view(), name='products-by-collection'),
#     path('collections/<int:collection_id>/variants/', VariantsByCollectionView.as_view(), name='variants-by-collection'),
#     path('categories/<int:category_id>/variants/', VariantsByCategoryView.as_view(), name='variants-by-category'),
]
