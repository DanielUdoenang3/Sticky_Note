from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'forms-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'forms-control my-3'})
        }
        labels = {
            "text":'Write your thoughts'
        }