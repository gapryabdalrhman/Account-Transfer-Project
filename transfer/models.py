from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
       return f"{self.name} ({self.id})"
