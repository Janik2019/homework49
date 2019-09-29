from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TaskForm, StatusForm, TypeForm

from webapp.models import Task, Type, Status

from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    # extra_context = {'tasks':Task.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return  context


class TaskCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'create.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={
                'form': form
            })


class TaskUpdateView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data={
            'title': task.title,
            'text': task.text,
            'status': task.status,
            'type': task.type
        })
        return render(request, 'update.html', context={'form': form, 'task': task})

    def post(self, request,  *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.text = form.cleaned_data['text']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'delete.html', {'task': task})

    def post(self, request,  *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')