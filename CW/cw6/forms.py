from django import forms
from .models import Day

class SelectDay (forms.Form):
    date = forms.ModelChoiceField(queryset=Day.objects.all(), empty_label="select date", to_field_name='date')
