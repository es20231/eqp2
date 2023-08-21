from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
class PasswordUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
    
class ProfileForm(forms.ModelForm):
    foto_de_perfil = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['foto_de_perfil', 'descricao_de_perfil']