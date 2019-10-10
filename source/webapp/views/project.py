from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectIndex(ListView):
    template_name = 'project/project.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'created_at'


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project
    context_key = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['project'].tasks.order_by('-created_at')
        context['tasks'] = tasks
        return context


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/project_create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})



class ProjectUpdateView(UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('project')
    model = Project
    context_object_name = 'project'


