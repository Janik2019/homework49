from webapp.forms import StatusForm
from django.urls import reverse, reverse_lazy
from webapp.models import Status

from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusView(ListView):
    template_name = 'status/status.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(LoginRequiredMixin,CreateView):
    model = Status
    template_name = 'status/status_create.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'status/status_update.html'
    form_class = StatusForm
    success_url = reverse_lazy('status')
    model = Status
    context_object_name = 'status'


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    form_class = StatusForm
    template_name = 'status/status_delete.html'
    success_url = reverse_lazy('status')
    model = Status
    context_object_name = 'status'
