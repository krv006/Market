from rest_framework.generics import ListCreateAPIView

from shops.models import Category, Product
from shops.serializers import CategoryModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CategoryModelSerializer
