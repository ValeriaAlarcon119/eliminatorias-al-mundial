from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Selection, Player

# Create your views here.
class SelectionListView(ListView):
    model = Selection

class SelectionDetailView(DetailView):
    model = Selection

class PlayerListView(ListView):
    model = Player

class PlayerDetailView(DetailView):
    model = Player