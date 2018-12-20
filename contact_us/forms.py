from django import forms
from .models import GetUserData


class UserData(forms.ModelForm):
    class Meta:
        model = GetUserData
        fields = [
            'Name',
            'Email',
            'Phone',
            'Interest',
            'Message',
        ]
