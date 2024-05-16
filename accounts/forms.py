from django import forms
from .models import CustomUser
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class SignUpForm(forms.ModelForm):
    name = forms.CharField(label=("Name"), max_length=255, required=False)
    email = forms.EmailField(label=("Email"), max_length=254, required=True)
    password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput, help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=("Password confirmation"),strip=False, widget=forms.PasswordInput, help_text=("Enter the same password as above, for verification."))

    class Meta:
        model= get_user_model()
        fields=['name', 'email']

class UserUpdateForm(forms.ModelForm):
    name=forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ('name')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']


