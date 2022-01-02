from django.db import models


class Extrasens(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя экстрасенса", unique=True)
    rating = models.IntegerField()