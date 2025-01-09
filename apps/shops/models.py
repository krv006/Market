from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Model, CharField, DecimalField, TextField, ForeignKey, CASCADE, ManyToManyField, \
    PositiveIntegerField
from django.utils.timezone import now

from shared.model import TimeBasedModel, SlugBasedModel


class Category(SlugBasedModel):
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = 'name',

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=255, verbose_name="Teg nomi")

    class Meta:
        verbose_name = "Teg"
        verbose_name_plural = "Teglar"
        ordering = 'name',

    def __str__(self):
        return self.name


class Product(TimeBasedModel):
    name = CharField(max_length=255, verbose_name="Mahsulot nomi")
    price = DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text='Narxini kiriting',
        verbose_name="Narxi"
    )
    description = TextField(
        help_text="Mahsulotni qisqacha ta'riflab bering",
        verbose_name="Ta'rif"
    )
    price_percentage = DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        verbose_name="Chegirma foizi"
    )
    quantity = PositiveIntegerField(
        default=0,
        help_text="Mahsulot sonini kiriting",
        verbose_name="Miqdor"
    )
    tags = ManyToManyField(
        'shops.Tag',
        related_name='products',
        verbose_name="Teglar"
    )
    category = ForeignKey(
        'shops.Category',
        CASCADE,
        related_name='products',
        verbose_name="Kategoriya"
    )

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = 'name',

    def __str__(self):
        return f"({self.id}) - {self.name} - {self.price} so'm"

    @property
    def new_price(self):
        return self.price * (100 - self.price_percentage) // 100

    @property
    def is_new(self) -> bool:
        return self.created_at >= now() - timedelta(days=7)

    @property
    def sub_amount(self):
        return self.price * self.quantity
