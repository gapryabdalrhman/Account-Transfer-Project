from django.test import TestCase
from .models import Account

class AccountTests(TestCase):
    def test_transfer_funds(self):
        acc1 = Account.objects.create(name="Alice", id="123", balance=100)
        acc2 = Account.objects.create(name="Bob", id="456", balance=50)
        acc1.balance -= 30
        acc2.balance += 30
        acc1.save()
        acc2.save()
        self.assertEqual(acc1.balance, 70)
        self.assertEqual(acc2.balance, 80)

