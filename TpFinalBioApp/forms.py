from django import forms

from .models import FastaFile


class SecuenceForm(forms.ModelForm):
    class Meta:
        model = FastaFile
        fields = ('file',)