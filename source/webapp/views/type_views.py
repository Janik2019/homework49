from webapp.forms import TypeForm
from django.urls import reverse
from webapp.models import Type

from django.views.generic import View, TemplateView, ListView,CreateView


from .base_views import DetailView, UpdateView, DeleteView



class TypeView(ListView):
    template_name = 'type/type.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    model = Type
    template_name = 'type/type_create.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type')


class TypeUpdateView(UpdateView):
    template_name = 'type/type_update.html'
    form_class = TypeForm
    redirect_url = 'type'
    model = Type
    context_object_name = 'type'



class TypeDeleteView(DeleteView):
    form_class = TypeForm
    template_name = 'type/type_delete.html'
    redirect_url = 'type'
    model = Type
    context_object_name = 'type'
