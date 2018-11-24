from django.shortcuts import render
from django.views.generic import (
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView,
    TemplateView,
    ListView
)


class Index(TemplateView):
    pass

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
    
    model = Plot

search_plot = SearchPlot.as_view()