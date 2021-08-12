from datetime import date
from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Owner name: {self.name}"

class Car(models.Model):
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.DateField(default=date(year=1950, month=1, day=1))
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type}, {self.model}, made on {self.year}"
