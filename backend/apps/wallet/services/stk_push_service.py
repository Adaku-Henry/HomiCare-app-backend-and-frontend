from ..models import Wallet, Transaction

class WalletService:

    def get_wallet(user):
        wallet, created = Wallet.objects.get_or_create(user=user)
        return wallet

    def credit_wallet(wallet, amount, reference=""):
        wallet.balance += amount
        wallet.save()

        Transaction.objects.create(
            wallet=wallet,
            type="TOPUP",
            amount=amount,
            status="SUCCESS",
            reference=reference
        )

    def debit_wallet(wallet, amount, reference=""):
        if wallet.balance < amount:
            raise Exception("Insufficient balance")

        wallet.balance -= amount
        wallet.save()

        Transaction.objects.create(
            wallet=wallet,
            type="WITHDRAW",
            amount=amount,
            status="SUCCESS",
            reference=reference
        )