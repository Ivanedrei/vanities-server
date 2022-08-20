from django.db import models


class Wood(models.Model):

    label = models.CharField(max_length=20)
