from django.core import validators
from django import forms
from .models import User

class Expense(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','date','amount','note'] 