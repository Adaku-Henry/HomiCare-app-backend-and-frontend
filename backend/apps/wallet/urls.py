from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WalletViewSet, WalletTransactionViewSet

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'transactions', WalletTransactionViewSet, basename='wallettransaction')


class WalletView(object):
    pass


class WithdrawView(object):
    pass


class TopUpView(object):
    pass


urlpatterns = [
    path('', include(router.urls)),
    path("wallet/", WalletView.as_view()),
    path("wallet/topup/", TopUpView.as_view()),
    path("wallet/withdraw/", WithdrawView.as_view()),
]
