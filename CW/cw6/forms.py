from django import forms
from .models import Day

class SelectDay (forms.Form):
    date = forms.ModelChoiceField(queryset=Day.objects.all(), empty_label="select date", to_field_name='date')

#class SelectDay (forms.ModelForm):
#    class Meta:
#        model = Day
#        fields = ['date']
#        widgets = {
#            'date' : forms.Select(attrs=(), choices=date)
#        }

#class TestDay (forms.ModelForm):
#    date = ModelChoiceField(queryset=Day.objects.all())
#    class Meta:
#        model = Day
#        fields = ['date']

#
#        widgets = {
#            'date': ModelChoiceField(queryset=Day.objects.all()),
#        }
       # date = forms.ModelChoiceField(queryset=Day.objects.all())

#class SelectDay (forms.ModelChoiceField):
#    class Meta:
#        model = Day
#        fields = ['date']