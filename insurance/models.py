from django.db import models


class Insurance(models.Model):
    type = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False)
    period = models.SmallIntegerField(null=False)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'insurance'


class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=100, null=False)
    age = models.PositiveSmallIntegerField(null=False)
    bank_id = models.BigIntegerField(unique=True, null=False)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'client'
