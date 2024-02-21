from rest_framework import serializers
from .models import Shop, Guard, Seller, Buyer, Product

class GuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guard
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    shops = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all(), many=True)

    class Meta:
        model = Product
        fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
    shops = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all(), many=True)

    class Meta:
        model = Buyer
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    guards = GuardSerializer(many=True, read_only=True)
    sellers = SellerSerializer(many=True, read_only=True)
    buyers = serializers.SlugRelatedField(slug_field='name', queryset=Buyer.objects.all(), many=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'