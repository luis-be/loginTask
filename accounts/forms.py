from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('correo_electronico', 'nombre_de_usuario', 'edad')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'nombre_de_usuario',
            'correo_electronico',
            'edad',
        )