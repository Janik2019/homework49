from django import forms
from django.forms import widgets
from webapp.models import Status, Type, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']
