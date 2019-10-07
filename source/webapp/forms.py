from django import forms
from django.forms import widgets
from webapp.models import Status, Type, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at']
    #
    # title = forms.CharField(max_length=40, label='Заголовок', required=True)
    # text = forms.CharField(max_length=3000, label='Описание', required=False, widget=widgets.Textarea)
    # status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус задачи', to_field_name='status')
    # type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Тип задачи', to_field_name='type')


# class StatusForm(forms.Form):
#     status = forms.CharField(max_length=50, label='Статус задачи')
#
#
# class TypeForm(forms.Form):
#     type = forms.CharField(max_length=50, label='Тип задачи')


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']
