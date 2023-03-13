from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    namecategory = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = 'Product Categories'
    def __str__(self):
        return self.namecategory

class Product(models.Model):
    nameproduct = models.CharField(max_length=256)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameproduct} | {self.category}'