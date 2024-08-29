from django import forms

class InputForm1(forms.Form):
    input1 = forms.IntegerField(label='Enter a number')