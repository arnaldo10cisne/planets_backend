from django.db import models

class Planet(models.Model):
  name=models.CharField(max_length=256)
  mass=models.CharField(max_length=256)
  number_of_moons=models.IntegerField()
  is_gas_giant=models.BooleanField()
