from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Пароль (повторно)')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')