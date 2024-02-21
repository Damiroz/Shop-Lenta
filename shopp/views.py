from rest_framework import generics
from .models import Shop, Guard, Seller, Buyer
from .serializers import ShopSerializer, GuardSerializer, SellerSerializer, BuyerSerializer

class ShopListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class GuardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Guard.objects.all()
    serializer_class = GuardSerializer

class GuardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guard.objects.all()
    serializer_class = GuardSerializer

class SellerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SellerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class BuyerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class BuyerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer