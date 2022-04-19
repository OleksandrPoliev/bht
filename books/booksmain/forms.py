from django import forms

from booksmain.Validators import ISBN_validator
from booksmain.models import BooksModel


class AddPostForm(forms.ModelForm):
    class Meta:
        model=BooksModel
        fields='__all__'
