from django import forms
from .models import Book, Student, Student2, Club


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating', 'publisher', 'authors']

        widgets = {
            'pubdate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'authors': forms.SelectMultiple(),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple()
        }


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'image']

