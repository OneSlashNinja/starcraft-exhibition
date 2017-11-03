from django.db import models

# Create your models here.


class Unit(models.Model):
    name = models.CharField(max_length=40)
    mineral_cost = models.IntegerField()
    gas_cost = models.IntegerField()
    supply_cost = models.IntegerField()
    damage = models.IntegerField()
    attack_range = models.IntegerField()
    cooldown = models.DecimalField(max_digits=10, decimal_places=2)
    speed = models.DecimalField(max_digits=12, decimal_places=4)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
