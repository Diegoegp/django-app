from django.db import models


class User(models.Model):
    user = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.password)

class Moroso(models.Model):
    name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    cellphone = models.CharField(max_length=255, null=False)
    no_apto = models.CharField(max_length=255, null=False)
    balance = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, null=False)
    date = models.CharField(max_length=255, null=False)
    comment = models.CharField(max_length=255, null=False)
    month = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.last_name, self.cellphone, self.no_apto, self.balance, self.status, self.date, self.comment, self.month)

