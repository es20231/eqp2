from django import forms
from .models import Profile


# Create a ProfileUpdateForm to update image.
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto_de_perfil', 'descricao_de_perfil']