from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
 
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

from django import forms
from .models import Record

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['medicine_name', 'medicine_description','medicine_price']
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['medicine_name', 'medicine_description', 'medicine_price']