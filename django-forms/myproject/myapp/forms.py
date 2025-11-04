from django import forms
from .models import users

class UsersModelForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['firstName','secondName','age']