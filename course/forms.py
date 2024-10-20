from django import forms
from django.contrib.auth.models import User

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
