from django import forms

class inputform1(forms.Form):
    input1=forms.IntegerField(label='Enter a start number')
    input2=forms.IntegerField(label='Enter a end number')