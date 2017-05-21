from django import forms
from django.contrib.auth.models import User





class UserrForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email','password')
