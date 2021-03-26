from django import forms
from .models import ProfileUser


class ProfileUserChangeForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'email', 'phone_number', 'address', 'inn')


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, max_length=20, label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = ProfileUser
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']
