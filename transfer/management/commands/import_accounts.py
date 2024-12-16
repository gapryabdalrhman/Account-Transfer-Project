import csv
from django.core.management.base import BaseCommand
from transfer.models import Account

class Command(BaseCommand):
    help = 'Import accounts from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help=r'Account Transfer Project\ accounts.csv')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Account.objects.create(
                    name=row['Name'],
                    account_number=row['ID'],
                    balance=row['Balance']
                )
        self.stdout.write(self.style.SUCCESS('Accounts imported successfully!'))
