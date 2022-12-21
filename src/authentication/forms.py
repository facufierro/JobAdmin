from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import custom_user


class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(max_length=30, required=True, help_text="Required.")
    phone = forms.CharField(max_length=30, required=True, help_text="Required.")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")

    class Meta:
        model = custom_user
        fields = UserCreationForm.Meta.fields + ("address", "phone")
