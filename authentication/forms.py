from django import forms
from django.core.exceptions import ValidationError
from authentication.models import User, AllowedEmail


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Проверяем, есть ли email в списке разрешённых
        if not AllowedEmail.objects.filter(email=email).exists():
            raise ValidationError(f"Регистрация с email {email} запрещена.")

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
