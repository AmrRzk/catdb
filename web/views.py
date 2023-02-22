from django.views.generic import TemplateView, ListView, DetailView

from .models import Human, Cat, Breed, Home


class IndexView(TemplateView):
    template_name = "index.html"


class HumanListView(ListView):
    model = Human
    template_name = 'listview.html'


class HumanDetailView(DetailView):
    model = Human
    template_name = 'detailview.html'


class CatListView(ListView):
    model = Cat
    template_name = 'listview.html'


class CatDetailView(DetailView):
    model = Cat
    template_name = 'detailview.html'


class HomeListView(ListView):
    model = Home
    template_name = 'listview.html'


class HomeDetailView(DetailView):
    model = Home
    template_name = 'Detailview.html'


class BreedListView(ListView):
    model = Breed
    template_name = 'listview.html'


class BreedDetailView(DetailView):
    model = Breed
    template_name = 'detailview.html'
