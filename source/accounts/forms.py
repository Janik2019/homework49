from django import forms


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Логин', required=True)
    password = forms.CharField(max_length=100, label='Пароль', required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='Подтверждение пароля', required=True,
                                       widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100, required=False, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    email = forms.EmailField(label='Емейл', required=False)

