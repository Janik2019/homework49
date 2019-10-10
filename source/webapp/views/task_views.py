from webapp.forms import TaskForm
from django.urls import reverse
from webapp.models import Task
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from .base_views import DetailView


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
    model = Task
    template_name = 'tracker/update.html'
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view',kwargs={'pk': self.object.pk})



class TaskDeleteView(DeleteView):
    template_name = 'tracker/delete.html'
    success_url = reverse_lazy('index')
    model = Task
    context_object_name = 'task'
