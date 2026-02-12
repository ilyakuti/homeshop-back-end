from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Product (models.Model):
    image_product = models.ImageField (upload_to="image_product/", default="product3.jpg", verbose_name="Image", blank=True)
    image_in_detail_1 = models.ImageField (upload_to="image_product/", default="product3.jpg", verbose_name="Image in detail 1", blank=True)
    image_in_detail_2 = models.ImageField (upload_to="image_product/", default="product3.jpg", verbose_name="Image in detail 2", blank=True)
    image_in_detail_3 = models.ImageField (upload_to="image_product/", default="product3.jpg", verbose_name="Image in detail 3", blank=True)
    short_name_product = models.CharField(max_length=127, null=True, verbose_name="Short Name Product")
    full_name_product = models.CharField (max_length=2047, null=True, verbose_name="Full Name Product")
    price_product = models.DecimalField (max_digits=6, decimal_places=2, null=True, verbose_name="Price")
    product_description = models.TextField (max_length=2047, null=True, verbose_name="Description")
    brand_product = models.CharField (max_length=127, null=True, verbose_name="Brand")
    color_product = models.CharField (max_length=127, null=True, verbose_name="Color")
    connectivity_product = models.CharField (max_length=127, null=True, verbose_name="Connectivity")
    battery_product = models.CharField (max_length=127, blank=True, null=True, verbose_name="Battery")
    in_stock = models.BooleanField()

class Person(AbstractUser):
    email = models.CharField(max_length=127, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)