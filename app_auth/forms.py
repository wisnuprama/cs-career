from django import forms
from .csui_helper import verify_user


class LoginForm(forms.Form):
    error_messages = {
        'required': 'This is a required field',
    }

    username_attrs = {
        'type': 'text',
        'class': 'login-form-input',
        'id': 'username-input',
        'name': 'username-input',
        'cols': 50,
        'placeholder': 'SSO Username',
    }

    password_attrs = {
        'type': 'password',
        'cols': 50,
        'class': 'login-form-input',
        'id': 'password-input',
        'name': 'password-input',
        'placeholder': 'SSO Password',
    }

    username = forms.CharField(label='Username SSO', required=True, widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(label='Password SSO', required=True, widget=forms.TextInput(attrs=password_attrs))
