from django.db import models

class market(models.Model):
    ticker = models.CharField(max_length=5)
    volume = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()

    def __str__(self):
        return self.ticker