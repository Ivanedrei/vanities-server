from turtle import width
from django.db import models


class Size(models.Model):

    width = models.DecimalField(max_digits=5, decimal_places=3)
