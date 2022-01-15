from django import forms


class CalcForm(forms.Form):
    calc = forms.CharField(label='Calculate')
