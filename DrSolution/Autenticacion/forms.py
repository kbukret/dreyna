from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPersonalizado


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ("grupoinforme", "empresa")


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = UsuarioPersonalizado
        fields = UserChangeForm.Meta.fields
        help_texts = {k: "" for k in fields}
