from django import forms
from.models import login
class todoform(forms.ModelForm):
    class Meta:
        model=login
        fields=['username','password','email']