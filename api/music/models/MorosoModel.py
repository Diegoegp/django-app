from django.db import models
from django.utils.timezone import now

class User(models.Model):
    user = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.password)

class Moroso(models.Model):
    name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    cellphone = models.BigIntegerField()
    no_apto = models.BigIntegerField()
    balance = models.BigIntegerField()
    status = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(default=now, blank=True)
    comment = models.CharField(max_length=255, null=False)
    month = models.BigIntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.last_name, self.cellphone, self.no_apto, self.balance, self.status, self.date, self.comment, self.month)

