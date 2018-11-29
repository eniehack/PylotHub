from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import \
    DetailView, CreateView, UpdateView, DeleteView, TemplateView, ListView

from .models import Plot
from .forms import CreateForm


class Index(TemplateView):
    template_name = 'plot/index.html'


index = Index.as_view()


class ViewPlot(DetailView):
    pass


view_plot = ViewPlot.as_view()


class CreatePlot(CreateView):

    model = Plot
    form_class = CreateForm
    template_name = 'plot/create.html'
    success_url = reverse_lazy('plot:index')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        result = super().form_valid(form)
        messages.success(self.request, 'have created your new post!')
        return result


create_plot = CreatePlot.as_view()


class EditPlot(UpdateView):
    pass


edit_plot = EditPlot.as_view()


class DeletePlot(DeleteView):
    pass


delete_plot = DeletePlot.as_view()


class SearchPlot(ListView):
    pass


search_plot = SearchPlot.as_view()
