from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TaskForm, StatusForm, TypeForm
from django.urls import reverse
from webapp.models import Task, Type, Status

from django.views.generic import View, TemplateView, ListView,CreateView


from .base_views import DetailView, UpdateView

# БАЗОВЫЕ КОНТРОЛЛЕРЫ


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1


class TaskView(DetailView):
    template_name = 'task.html'
    model = Task
    context_key = 'task'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('index')


class TaskUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = TaskForm
    # redirect_url = 'task_view'
    model = Task
    context_object_name = 'task'

    def get_redirect_url(self):
        return reverse('task_view',kwargs={'pk': self.obj.pk})



# class TaskUpdateView(View):
#     def get(self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs.get('pk'))
#         form = TaskForm(data={
#             'title': task.title,
#             'text': task.text,
#             'status': task.status,
#             'type': task.type
#         })
#         return render(request, 'update.html', context={'form': form, 'task': task})
#
#     def post(self, request,  *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs.get('pk'))
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task.title = form.cleaned_data['title']
#             task.text = form.cleaned_data['text']
#             task.status = form.cleaned_data['status']
#             task.type = form.cleaned_data['type']
#             task.save()
#             return redirect('task_view', pk=task.pk)
#         else:
#             return render(request, 'update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'delete.html', {'task': task})

    def post(self, request,  *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')


# Контроллеры для вывода ТИПОВ

class TypeView(ListView):
    template_name = 'type.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    model = Type
    template_name = 'type_create.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type')


class TypeUpdateView(UpdateView):
    template_name = 'type_update.html'
    form_class = TypeForm
    redirect_url = 'type'
    model = Type
    context_object_name = 'type'


    # def get(self, request, *args, **kwargs):
    #     type = get_object_or_404(Type, pk=kwargs.get('pk'))
    #     form = TypeForm(data={
    #         'type': type.type
    #     })
    #     return render(request, 'type_update.html', context={'form': form, 'type': type})
    #
    # def post(self, request,  *args, **kwargs):
    #     type = get_object_or_404(Type, pk=kwargs.get('pk'))
    #     form = TypeForm(data=request.POST)
    #     if form.is_valid():
    #         type.type = form.cleaned_data['type']
    #         type.save()
    #         return redirect('type')
    #     else:
    #         return render(request, 'type_update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        return render(request, 'type_delete.html', {'type': type})

    def post(self, request,  *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        type.delete()
        return redirect('type')


# КОНТРОЛЛЕРЫ ДЛЯ ВЫВОДА СТАТУСОВ


class StatusView(ListView):
    template_name = 'status.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    model = Status
    template_name = 'status_create.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status')



class StatusUpdateView(UpdateView):
    template_name = 'status_update.html'
    form_class = StatusForm
    redirect_url = 'status'
    model = Status
    context_object_name = 'status'

    # def get(self, request, *args, **kwargs):
    #     status = get_object_or_404(Status, pk=kwargs.get('pk'))
    #     form = StatusForm(data={
    #         'status': status.status
    #     })
    #     return render(request, 'status_update.html', context={'form': form, 'status': status})
    #
    # def post(self, request,  *args, **kwargs):
    #     status = get_object_or_404(Status, pk=kwargs.get('pk'))
    #     form = StatusForm(data=request.POST)
    #     if form.is_valid():
    #         status.status = form.cleaned_data['status']
    #         status.save()
    #         return redirect('status')
    #     else:
    #         return render(request, 'status_update.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(request, 'status_delete.html', {'status': status})

    def post(self, request,  *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()
        return redirect('status')
