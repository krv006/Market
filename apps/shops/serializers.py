from rest_framework.serializers import ModelSerializer

from shops.models import Category, Product, Tag


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',


class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = 'id', 'name',


class ProductModelSerializer(ModelSerializer):
    category = CategoryModelSerializer()
    tags = TagModelSerializer()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'price', 'description', 'price_percentage', 'quantity', 'created_at', 'updated_at',
            'category',
            'tags',)
