from django.db import models


class Phone(models.Model):
    name = models.TextField(null=False)
    price = models.FloatField(null=False)
    image = models.TextField()
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length=150, unique=True)

