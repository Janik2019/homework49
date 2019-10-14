from webapp.forms import TaskForm, SimpleSearchForm
from django.urls import reverse
from webapp.models import Task
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from .base_views import DetailView

from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(text__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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
