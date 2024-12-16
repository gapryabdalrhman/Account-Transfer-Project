from django.shortcuts import render
from .models import Account
from rest_framework import viewsets,status
from . serializers import AccountSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from decimal import Decimal


def transfer_funds_page(request):
    return render(request, 'transfer_funds.html')


class Accountviewset(viewsets.ModelViewSet):  
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(detail=False, methods=['post'], url_path='transfer-funds')
    def transfer_funds(self, request):
        source_account_id = request.data.get('source_account_id')
        target_account_id = request.data.get('target_account_id')
        amount = request.data.get('amount')

        
        if not all([source_account_id, target_account_id, amount]):
            return Response(
                {"error": "source_account_id, target_account_id, and amount are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            amount = Decimal(amount)  
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            source_account = Account.objects.select_for_update().get(id=source_account_id)
            target_account = Account.objects.select_for_update().get(id=target_account_id)

            
            if source_account.balance < amount:
                return Response({"error": "Insufficient funds in the source account."}, status=status.HTTP_400_BAD_REQUEST)

            
            source_account.balance -= amount
            target_account.balance += amount
            source_account.save()
            target_account.save()

        except Account.DoesNotExist:
            return Response({"error": "One or both accounts do not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "Transaction failed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            {
                "message": f"Successfully transferred {amount} from Account {source_account_id} to Account {target_account_id}."
            },
            status=status.HTTP_200_OK
        )