from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class DisciplineCreateForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'education': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'teacher': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Название'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    age = forms.DateField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'firstname', 'lastname', 'dadname', 'image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'dadname': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'age': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


def year_choices():
    return [(r,r) for r in range(2018, datetime.date.today().year+5)]


def current_year():
    return datetime.date.today().year


class IndexForm(forms.ModelForm):

    class Meta:
        model = Index
        exclude = ['teacher', 'discripline', 'bally', 'data']
        fields = '__all__'


class IndexAdminForm(forms.ModelForm):

    class Meta:
        model = Index
        exclude = ['teacher', 'discripline', 'data']
        fields = '__all__'


class WordGenForm(forms.Form):
    data = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
