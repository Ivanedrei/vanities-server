from django.db import models
from vanitiesapi.models.vanities import Vanities
from vanitiesapi.models.orders import Order


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Vanities, on_delete=models.CASCADE)
