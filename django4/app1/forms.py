from django import forms
from app1.models import students

class studentform1(forms.ModelForm):
    class Meta:
        model=students
        fields=['name','course','college']