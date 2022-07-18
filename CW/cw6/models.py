from django.db import models

class Days (models.Model):
    #date = models.DateField(blank=False)
    date = models.CharField(max_length=10,help_text='first day',blank=True)
    d1 = models.CharField(max_length=4)
    d2 = models.IntegerField()
    d3 = models.IntegerField
    d4 = models.IntegerField
    d5 = models.IntegerField
    d6 = models.IntegerField
    d7 = models.IntegerField

    def __str__(self):
        return self.date

# Create your models here.
