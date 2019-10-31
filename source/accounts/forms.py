from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=50, label='Логин', required=True)
    password = forms.CharField(max_length=50, label='Пароль', required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=50, label='Подтверждение пароля', required=True,
                                       widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, required=False, label='Имя')
    last_name = forms.CharField(max_length=50, required=False, label='Фамилия')
    email = forms.EmailField(label='Емейл', required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Такой пользователь уже существует',
                                  code='user_exists')
        except User.DoesNotExist:
            return username

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if password_1 != password_2:
            raise ValidationError('Пароли не совпадают', code='passwords_do_not_match')
        elif not first_name and not last_name:
            raise ValidationError('Поле имени или фамилии должно быть заполнено', code='last_name_firs_name_error')
        return self.cleaned_data


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}



