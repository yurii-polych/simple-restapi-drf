from django.db import models


class Insurance(models.Model):
    type = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False)
    period = models.SmallIntegerField(null=False)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'insurance'

    def __str__(self):
        return f'{self.pk}. type: {self.type}, name: {self.name}, price: {self.price}'


class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=100, null=False)
    age = models.PositiveSmallIntegerField(null=False)
    bank_id = models.BigIntegerField(unique=True, null=False)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'client'


class Logs(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    lest_name = models.CharField(max_length=100, null=False)
    age = models.PositiveSmallIntegerField(null=False)
    bank_id = models.BigIntegerField(null=False)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, null=False)
    action = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'logs'
