from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=127, null=False)
    last_name = models.CharField(max_length=127, null=False)
    username = models.CharField(max_length=127, null=False)
    mail = models.EmailField(max_length=127, null=False)
    password = models.CharField(max_length=127, null=False)
