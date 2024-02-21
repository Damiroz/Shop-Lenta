from django.urls import path, include
from django.contrib import admin
from .views import (
    ShopListCreateAPIView,
    ShopDetailAPIView,
    GuardListCreateAPIView,
    GuardDetailAPIView,
    SellerListCreateAPIView,
    SellerDetailAPIView,
    BuyerListCreateAPIView,
    BuyerDetailAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs для магазинов
    path('shops/', ShopListCreateAPIView.as_view(), name='shop-list'),
    path('shops/<int:pk>/', ShopDetailAPIView.as_view(), name='shop-detail'),

    # URLs для охранников
    path('guards/', GuardListCreateAPIView.as_view(), name='guard-list'),
    path('guards/<int:pk>/', GuardDetailAPIView.as_view(), name='guard-detail'),

    # URLs для продавцов
    path('sellers/', SellerListCreateAPIView.as_view(), name='seller-list'),
    path('sellers/<int:pk>/', SellerDetailAPIView.as_view(), name='seller-detail'),

    # URLs для покупателей
    path('buyers/', BuyerListCreateAPIView.as_view(), name='buyer-list'),
    path('buyers/<int:pk>/', BuyerDetailAPIView.as_view(), name='buyer-detail'),
]