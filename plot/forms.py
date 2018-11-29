from django import forms

from .models import Plot


class CreateForm(forms.ModelForm):

    class Meta:
        model = Plot
        fields = ['title', 'genre', 'content']
