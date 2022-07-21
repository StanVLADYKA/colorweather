from django.db import models


class Days (models.Model):
    date = models.DateField(help_text='first day',blank=True)
    d1 = models.IntegerField(blank=True,null=True)
    d2 = models.IntegerField(blank=True,null=True)
    d3 = models.IntegerField(blank=True,null=True)
    d4 = models.IntegerField(blank=True,null=True)
    d5 = models.IntegerField(blank=True,null=True)
    d6 = models.IntegerField(blank=True,null=True)
    d7 = models.IntegerField(blank=True,null=True)

    #def __str__(self):
    #    return self.date

# Create your models here.
