from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCustomerRegister(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','email', 'phone', 'password1', 'password2']


class ContactUs(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
