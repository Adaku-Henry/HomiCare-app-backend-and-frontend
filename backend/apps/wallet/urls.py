from django.urls import path, include

from .views import (
    WalletView,
    WalletTopUpView,
    WalletSpendView,
    WithdrawalRequestView
)

urlpatterns = [
    path("wallet/", WalletView.as_view(), name="wallet"),
    path("wallet/topup/", WalletTopUpView.as_view(), name="wallet-topup"),
    path("wallet/spend/", WalletSpendView.as_view(), name="wallet-spend"),
    path("wallet/withdraw/", WithdrawalRequestView.as_view(), name="wallet-withdraw"),
]