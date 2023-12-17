from django.db import models

#prediction data model
class PredictionData(models.Model):
    RM = models.FloatField()
    LSTAT = models.FloatField()
    PTRATIO = models.FloatField()
         