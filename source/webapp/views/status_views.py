from webapp.forms import StatusForm
from django.urls import reverse
from webapp.models import Status

from django.views.generic import View, TemplateView, ListView,CreateView


from .base_views import DetailView, UpdateView, DeleteView

class StatusView(ListView):
    template_name = 'status/status.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    model = Status
    template_name = 'status/status_create.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status')


class StatusUpdateView(UpdateView):
    template_name = 'status/status_update.html'
    form_class = StatusForm
    redirect_url = 'status'
    model = Status
    context_object_name = 'status'


class StatusDeleteView(DeleteView):
    form_class = StatusForm
    template_name = 'status/status_delete.html'
    redirect_url = 'status'
    model = Status
    context_object_name = 'status'
