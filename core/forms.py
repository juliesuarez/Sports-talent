from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Player, Academy

class AcademyForm(forms.ModelForm):
    class Meta:
        model = Academy
        fields = ['name', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'position', 'academy']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'academy': forms.Select(attrs={'class': 'form-control'}),
        }

class TransferForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['academy'] # Only allow changing the academy
        labels = {
            'academy': 'Select New Academy to Transfer To'
        }
        widgets = {
            'academy': forms.Select(attrs={'class': 'form-control'})
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply the Tailwind form-control class to all auth fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'