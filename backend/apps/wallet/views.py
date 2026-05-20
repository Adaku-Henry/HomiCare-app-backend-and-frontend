from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Wallet, WalletTransaction, WithdrawalRequest

User = get_user_model()


# ----------------------------------------
# GET wallet balance + transactions
# ----------------------------------------
class WalletView(APIView):

    def get(self, request):
        wallet, created = Wallet.objects.get_or_create(user=request.user)

        transactions = wallet.transactions.all().order_by('-timestamp')

        data = {
            "balance": wallet.balance,
            "transactions": [
                {
                    "type": t.transaction_type,
                    "amount": t.amount,
                    "reference": t.reference,
                    "description": t.description,
                    "timestamp": t.timestamp,
                }
                for t in transactions
            ]
        }

        return Response(data, status=status.HTTP_200_OK)


# ----------------------------------------
# TOP UP WALLET
# ----------------------------------------
class WalletTopUpView(APIView):

    def post(self, request):
        wallet, _ = Wallet.objects.get_or_create(user=request.user)

        amount = request.data.get("amount")
        reference = request.data.get("reference", "TOPUP-REF")
        description = request.data.get("description", "")

        if not amount:
            return Response({"error": "Amount is required"}, status=400)

        wallet.topup(amount, reference, description)

        return Response({
            "message": "Top-up successful",
            "balance": wallet.balance
        }, status=200)


# ----------------------------------------
# SPEND FROM WALLET
# ----------------------------------------
class WalletSpendView(APIView):

    def post(self, request):
        wallet, _ = Wallet.objects.get_or_create(user=request.user)

        amount = request.data.get("amount")
        reference = request.data.get("reference", "SPEND-REF")
        description = request.data.get("description", "")

        if not amount:
            return Response({"error": "Amount is required"}, status=400)

        try:
            wallet.spend(amount, reference, description)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        return Response({
            "message": "Spend successful",
            "balance": wallet.balance
        }, status=200)


# ----------------------------------------
# WITHDRAW REQUEST
# ----------------------------------------
class WithdrawalRequestView(APIView):

    def post(self, request):
        wallet, _ = Wallet.objects.get_or_create(user=request.user)

        amount = request.data.get("amount")

        if not amount:
            return Response({"error": "Amount is required"}, status=400)

        withdrawal = WithdrawalRequest.objects.create(
            wallet=wallet,
            amount=amount
        )

        return Response({
            "message": "Withdrawal request submitted",
            "status": withdrawal.status
        }, status=201)


class WalletTransactionViewSet:
    pass