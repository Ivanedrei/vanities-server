from django.db import models


class VanityType(models.Model):

    label = models.CharField(max_length=20)
