from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Создание профиля с дополнительным полем is_admin
            profile = Profile(user=user, is_admin=self.cleaned_data.get('is_admin', False))
            profile.save()
        return user
