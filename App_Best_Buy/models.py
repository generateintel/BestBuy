from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=True)
    icon=models.TextField(blank=True)
    hide=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class Best_Buy(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_best_buy")
    model_number = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    sale_price = models.CharField(max_length=255, blank=True, null=True)
    regular_price = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Fluctuate_Price(models.Model):
    best_buy_product_id = models.ForeignKey(Best_Buy, on_delete=models.CASCADE, related_name="best_buy_price")
    price = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)