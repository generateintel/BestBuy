from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category , Best_Buy,Fluctuate_Price


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class Best_Buy_Serializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Best_Buy
        # fields='__all__'
        fields=['id','category','model_number', 'name','sku','image','sale_price','regular_price','is_active']
