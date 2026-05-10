from django.db import models

class FitnessData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    category = models.CharField(max_length=50)
    stress_level = models.IntegerField(null=True, blank=True)
    workout = models.CharField(max_length=200, null=True, blank=True)
    diet = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name