from webapp.forms import TaskForm
from django.urls import reverse
from webapp.models import Task

from django.views.generic import ListView,CreateView


from .base_views import DetailView, UpdateView, DeleteView

# БАЗОВЫЕ КОНТРОЛЛЕРЫ


class IndexView(ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1


class TaskView(DetailView):
    template_name = 'tracker/task.html'
    model = Task
    context_key = 'task'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tracker/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('index')


class TaskUpdateView(UpdateView):
    template_name = 'tracker/update.html'
    form_class = TaskForm
    # redirect_url = 'task_view'
    model = Task
    context_object_name = 'task'

    def get_redirect_url(self):
        return reverse('task_view',kwargs={'pk': self.obj.pk})



class TaskDeleteView(DeleteView):
    form_class = TaskForm
    template_name = 'tracker/delete.html'
    redirect_url = 'index'
    model = Task
    context_object_name = 'task'
