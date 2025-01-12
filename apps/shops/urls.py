from django.urls import path, include

from shops.views import CategoryListCreateAPIView, ProductListCreateAPIView, TagListCreateAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name='category'),
    path('product/', ProductListCreateAPIView.as_view(), name='product'),
    path('tag/', TagListCreateAPIView.as_view(), name='tag'),
]
