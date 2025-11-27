from django import forms
from .models import squawk
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SquawkForm(forms.ModelForm):
    class Meta:
        model = squawk
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What\'s on your mind?', 'rows': 4}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
