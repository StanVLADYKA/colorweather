from django import forms
from .models import Day

class SelectDay (forms.Form):
    date = forms.ModelChoiceField(queryset=Day.objects.all().order_by('date'), empty_label="select date")
