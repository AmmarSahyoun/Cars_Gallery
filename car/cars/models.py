from django.db import models

class car(models.Model):
    type = models.charField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.DateField()
