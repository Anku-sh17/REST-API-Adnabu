from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('categories/', views.category_list, name='category_list'), #List all the categories
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),  #List categories with specific id's
    path('products/', views.product_list, name='product_list'), #List all the prodcuts
    path('products/<int:pk>/', views.product_detail, name='product_detail'), #List products with specific id's
    path('collections/', views.collection_list, name='collection_list'), #List all the collections
    path('collections/<int:pk>/', views.collection_detail, name='collection_detail'), #List collections with specific id's
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Get the authetication token and refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # get the authetication token using refresh token
]
