from rest_framework.serializers import ModelSerializer

from shops.models import Category, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'id', 'name',
