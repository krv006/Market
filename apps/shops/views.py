from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from shops.models import Category, Product, Tag
from shops.serializers import CategoryModelSerializer, ProductModelSerializer, TagModelSerializer


@extend_schema(tags=['shops'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['shops'])
class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer


@extend_schema(tags=['shops'])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
