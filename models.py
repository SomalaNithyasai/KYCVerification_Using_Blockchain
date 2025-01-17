from django.db import models

class LocalStore(models.Model):
    userid=models.IntegerField()
    actor=models.CharField(max_length=30)
    