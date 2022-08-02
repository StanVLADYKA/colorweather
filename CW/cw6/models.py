from django.db import models

class Day(models.Model):
    date = models.CharField(max_length=10,help_text='first day', blank=True)
    d1 = models.CharField(max_length=3, blank=True, null=True)
    d2 = models.CharField(max_length=3, blank=True, null=True)
    d3 = models.CharField(max_length=3, blank=True, null=True)
    d4 = models.CharField(max_length=3, blank=True, null=True)
    d5 = models.CharField(max_length=3, blank=True, null=True)
    d6 = models.CharField(max_length=3, blank=True, null=True)
    d7 = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        date = f'date:{self.date},'
        d1 = f'd1: {self.d1}'
        d2 = f'd2: {self.d2}'
        d3 = f'd3: {self.d3}'
        d4 = f'd4: {self.d4}'
        d5 = f'd5: {self.d5}'
        d6 = f'd6: {self.d6}'
        return f'{date}'
#        return f'{date},{d1},{d2},{d3},{d4},{d5},{d6}'




