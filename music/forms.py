from django import forms
from .models import Song


class UploadSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'author', 'title', 'genre', 'file'
        ]
        labels = {
            'author': '',
            'title': '',
            'genre': '',
            'file': ''
        }
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True})
        }
        help_texts = {
            'author': 'Author',
            'title': 'Name of the song',
            'genre': 'Genre'
        }
