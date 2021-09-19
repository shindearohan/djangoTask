from django import forms
from nemesis.models import Sign

class empforms(forms.ModelForm):
    class Meta:
        model=Sign
        fields="__all__"
