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
