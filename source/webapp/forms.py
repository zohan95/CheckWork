from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'mail', 'details']


class RecordSearch(forms.Form):
    search_field = forms.CharField(max_length=100, label="Поиск")
