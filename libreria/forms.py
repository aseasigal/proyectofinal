from collections import UserDict
from django import forms
from .models import Alfajor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AlfajorForm(forms.ModelForm):
    class Meta:
        model = Alfajor
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir la Contraseña', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = 'Modifical E-mail')
    password1= forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)
    primer_nombre = forms.CharField()
    apellido = forms.CharField()

    class Meta:
        model = User
        fields= ['email','password1','password2', 'primer_nombre', 'apellido']
