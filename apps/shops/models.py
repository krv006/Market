from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya nomi")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = 'name',

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name="Teg nomi")

    class Meta:
        verbose_name = "Teg"
        verbose_name_plural = "Teglar"
        ordering = 'name',

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text='Narxini kiriting',
        verbose_name="Narxi"
    )
    description = models.TextField(
        help_text="Mahsulotni qisqacha ta'riflab bering",
        verbose_name="Ta'rif"
    )
    price_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        verbose_name="Chegirma foizi"
    )
    quantity = models.PositiveIntegerField(
        default=0,
        help_text="Mahsulot sonini kiriting",
        verbose_name="Miqdor"
    )
    tags = models.ManyToManyField(
        'shops.Tag',
        related_name='products',
        verbose_name="Teglar"
    )
    category = models.ForeignKey(
        'shops.Category',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Kategoriya"
    )

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = 'name',

    def __str__(self):
        return f"{self.name} - {self.price} so'm"
