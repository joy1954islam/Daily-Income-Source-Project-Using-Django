from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
                 'email',
                 'first_name',
                 'last_name',
                ]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'bio', 'image', 'Address']