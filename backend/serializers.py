from rest_framework import serializers

from backend.models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'url', 'filename',)


class ProductSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'quantity', 'price', 'shop',)
