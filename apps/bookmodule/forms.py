from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating', 'publisher', 'authors']

        widgets = {
            'pubdate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'authors': forms.SelectMultiple(),
        }