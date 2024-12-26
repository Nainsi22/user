from django import forms
from user_management.user_management.models import User  # Ensure the model name matches your actual model

class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Your model
        fields = '__all__'  # Use specific fields like ['name', 'email', 'password'] if needed
