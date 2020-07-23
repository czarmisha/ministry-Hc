from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               help_text='Не более 150 символов. Только буквы, цифры и символы @/./+/-/_',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CreateWorksheetForm(forms.ModelForm):

    class Meta:
        model = WorkSheet
        fields = ['first_name', 'last_name', 'birth_date', 'region', 'district', 'first_phone', 'second_phone',
                  'shifokor', 'hamshira', 'status']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'second_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'shifokor': forms.Select(attrs={'class': 'form-control'}),
            'hamshira': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
        }