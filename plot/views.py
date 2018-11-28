from django.shortcuts import render
from .models import Plot
from django.views.generic import \
    DetailView, CreateView, UpdateView, DeleteView, TemplateView, ListView


class Index(TemplateView):
    template_name = 'plot/index.html'

index = Index.as_view()

class ViewPlot(DetailView):
    pass

view_plot = ViewPlot.as_view()

class CreatePlot(CreateView):
    pass

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