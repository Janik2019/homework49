from django import forms
from webapp.models import Status, Type, Task, Project


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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project', 'description']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Поиск')
