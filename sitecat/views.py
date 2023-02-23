from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import HumanForm, CatForm, BreedForm, HomeForm
from .models import Human, Cat, Breed, Home


class IndexView(TemplateView):
    template_name = "index.html"


class Human:

    class List(ListView):
        model = Human
        template_name = 'listview.html'

    class Detail(DetailView):
        model = Human
        template_name = 'detailview.html'

    class Create(CreateView):
        form_class = HumanForm
        template_name = 'create.html'
        success_url = '/human'


class Cat:
    class List(ListView):
        model = Cat
        template_name = 'listview.html'

    class Detail(DetailView):
        model = Cat
        template_name = 'detailview.html'

    class Create(CreateView):
        form_class = CatForm
        template_name = 'create.html'
        success_url = '/cat'


class Home:
    class List(ListView):
        model = Home
        template_name = 'listview.html'

    class Detail(DetailView):
        model = Home
        template_name = 'Detailview.html'

    class Create(CreateView):
        form_class = HomeForm
        template_name = 'create.html'
        success_url = '/home'


class Breed:
    class List(ListView):
        model = Breed
        template_name = 'listview.html'

    class Detail(DetailView):
        model = Breed
        template_name = 'detailview.html'

    class Create(CreateView):
        form_class = BreedForm
        template_name = 'create.html'
        success_url = '/breed'
