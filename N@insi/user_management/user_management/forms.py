from django import forms
from .models import User  # Ensure the relative import matches your app's structure

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']  # Adjust fields as needed
