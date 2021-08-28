from datetime import date
from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the full name")
    mobile = models.IntegerField(default='0731111111')

    def __str__(self):
        return f"Owner name: {self.name}"


class Car(models.Model):
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField(default=1950)
    image = models.ImageField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Meta:
        ordering = ['model']

    def __str__(self):
        return f"{self.type}, {self.model}, made on {self.year}"
