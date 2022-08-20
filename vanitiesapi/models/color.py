from django.db import models


class Color(models.Model):

    label = models.CharField(max_length=20)
