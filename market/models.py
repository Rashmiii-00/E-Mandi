from django.db import models

class item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='itemImg')
    unit = models.CharField(max_length=100)
    price = models.IntegerField()


class cartItem(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
