from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'sign__input',
            'required': 'required',
            'placeholder': 'Foydalanuvchi nomi'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'sign__input',
            'required': 'required',
            'placeholder': 'Ism'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'sign__input',
            'required': 'required',
            'placeholder': 'Familya'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'sign__input',
            'required': 'required',
            'type': 'email',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'sign__input',
            'required': 'required',
            'placeholder': 'Parol'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'sign__input',
            'required': 'required',
            'placeholder': 'Parolni tasdiqlang'
        })
