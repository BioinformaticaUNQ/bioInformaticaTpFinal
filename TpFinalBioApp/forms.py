from django import forms

from .models import Secuencia


class SecuenceForm(forms.ModelForm):
    class Meta:
        model = Secuencia
        fields = ('adress', 'length', 'content', 'file')