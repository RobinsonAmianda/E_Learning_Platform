from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile

# Sign Up Form for both Student and Instructor
class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

# Login Form
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
