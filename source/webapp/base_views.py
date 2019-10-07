from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404, render, redirect


class DetailView(TemplateView):
    context_key = 'objects'
    model = None
    pk_url = 'pk'

    def get_context_data(self, **kwargs):
        pk = kwargs.get(self.pk_url)
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context

# class UpdateView(View):
#     form_classs = None
#     template_name = None
#     model = None
#     redirect_url = None
#
#     def get(self,re):

class UpdateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None
    pk_url = 'pk'
    context_object_name = None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk_url)
        self.obj = get_object_or_404(self.model, pk=kwargs.get('pk'))
        form = self.form_class(instance = self.obj)
        return render(request, self.template_name, context={'form': form, self.context_object_name: self.obj})

    def post(self, request, *args, **kwargs):
        self.obj =get_object_or_404(self.model, pk=kwargs.get('pk'))
        form = self.form_class(data=request.POST, instance=self.obj)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})
