from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Your Name'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Repeat your password'
        })

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email address'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })

class CustomPasswordResetForm(PasswordResetForm):
    def get_users(self, email):
        print(f"🔍 Перевіряємо користувача по email (username): {email}")
        users = User.objects.filter(username=email, is_active=True)
        print(f"🔍 Знайдено: {list(users)}")
        return users

    def save(self, *args, **kwargs):
        print("📤 Відправляємо лист через save()")
        return super().save(*args, **kwargs)