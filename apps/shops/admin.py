from django.contrib import admin
from django.contrib.admin import ModelAdmin

from shops.models import Product, Category, Tag


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass