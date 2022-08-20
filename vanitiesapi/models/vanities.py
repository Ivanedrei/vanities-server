from django.db import models
from vanitiesapi.models.color import Color
from vanitiesapi.models.size import Size
from vanitiesapi.models.vanity_type import VanityType
from vanitiesapi.models.wood import Wood


class Vanities(models.Model):

    type = models.ForeignKey(VanityType, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    wood = models.ForeignKey(Wood, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()
