from django import forms
from django.db import models
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib import messages

from .forms import HumanForm, CatForm, BreedForm, HomeForm
from .models import Human as HumanModel, Cat as CatModel, Breed as BreedModel, Home as HomeModel


class IndexView(TemplateView):
    template_name = "index.html"


def edit(request: HttpRequest, Form: forms.ModelForm, model: models.Model, url_name: str, id: int):
    if request.method == 'GET':
        context = {'form': Form(instance=model), 'id': id}
        return render(request, 'form.html', context)

    elif request.method == 'POST':
        form = Form(request.POST, instance=model)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been updated successfully.')
            return redirect(reverse(url_name, args=[id]))
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'form.html', {'form': form})


class Human:

    class List(ListView):
        model = HumanModel
        template_name = 'listview.html'

    class Detail(DetailView):
        model = HumanModel
        template_name = 'detailview.html'

    class Form(CreateView):
        form_class = HumanForm
        template_name = 'form.html'
        success_url = '/human'

    def edit_human(request, pk):
        human = get_object_or_404(HumanModel, id=pk)
        return edit(request, HumanForm, human, 'sitecat:human-detail', pk)


class Cat:
    class List(ListView):
        model = CatModel
        template_name = 'listview.html'

    class Detail(DetailView):
        model = CatModel
        template_name = 'detailview.html'

    class Form(CreateView):
        form_class = CatForm
        template_name = 'form.html'
        success_url = '/cat'

    def edit_cat(request, pk):
        cat = get_object_or_404(CatModel, id=pk)
        return edit(request, CatForm, cat, 'sitecat:cat-detail', pk)


class Home:
    class List(ListView):
        model = HomeModel
        template_name = 'listview.html'

    class Detail(DetailView):
        model = HomeModel
        template_name = 'detailview.html'

    class Form(CreateView):
        form_class = HomeForm
        template_name = 'form.html'
        success_url = '/home'

    def edit_home(request, pk):
        home = get_object_or_404(HomeModel, id=pk)
        return edit(request, HomeForm, home, 'sitecat:home-detail', pk)


class Breed:
    class List(ListView):
        model = BreedModel
        template_name = 'listview.html'

    class Detail(DetailView):
        model = BreedModel
        template_name = 'detailview.html'

    class Form(CreateView):
        form_class = BreedForm
        template_name = 'form.html'
        success_url = '/breed'

    def edit_breed(request, pk):
        breed = get_object_or_404(BreedModel, id=pk)
        return edit(request, BreedForm, breed, 'sitecat:breed-detail', pk)
