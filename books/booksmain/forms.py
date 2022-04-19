from django import forms
from .models import BooksModel


class AddPostForm(forms.ModelForm):
    class Meta:
        model=BooksModel
        fields='__all__'
