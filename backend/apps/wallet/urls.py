from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    WalletViewSet,
    WalletTransactionViewSet,
    WalletView,
    WalletTopUpView,
    WalletSpendView,
    WithdrawalRequestView
)

# -----------------------------------
# DRF ROUTER (ViewSets)
# -----------------------------------
router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'transactions', WalletTransactionViewSet, basename='wallettransaction')


# -----------------------------------
# URL PATTERNS
# -----------------------------------
urlpatterns = [
    # ViewSets routes
    path('', include(router.urls)),

    # Wallet endpoints
    path("wallet/", WalletView.as_view(), name="wallet"),
    path("wallet/topup/", WalletTopUpView.as_view(), name="wallet-topup"),
    path("wallet/spend/", WalletSpendView.as_view(), name="wallet-spend"),
    path("wallet/withdraw/", WithdrawalRequestView.as_view(), name="wallet-withdraw"),
]