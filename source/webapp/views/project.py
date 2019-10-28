from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project

from django.db.models import Q
from django.utils.http import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectIndex(ListView):
    template_name = 'project/project.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'created_at'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        print(self.get_search_form())
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        print(self.form)
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(project__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project
    context_key = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['project'].tasks.order_by('-created_at')
        context['tasks'] = tasks
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project/project_create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('project')
    model = Project
    context_object_name = 'project'


