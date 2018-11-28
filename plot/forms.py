from django import forms

from .models import Plot


class CreateForm(forms.ModelForm):

    class Meta:
        model = Plot
        fields = ['user_id', 'title', 'genre', 'content']
        widgets = {'user_id': forms.HiddenInput()}