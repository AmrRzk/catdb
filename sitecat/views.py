from django import forms
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib import messages

from .forms import HumanForm, CatForm, BreedForm, HomeForm
from .models import Human as HumanModel, Cat as CatModel, Breed as BreedModel, Home as HomeModel
from pprint import pprint

import pandas as pd
import io


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
                request, 'The record has been updated successfully.')
            return redirect(reverse(url_name, args=[id]))
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'form.html', {'form': form})


def delete(request: HttpRequest, model: models.Model, model_type: str, url: str, id: int):
    context = dict(zip((model_type, 'id'), (model, id)))
    if request.method == "POST":
        model.delete()
        messages.success(
            request, 'The record has been successfully deleted')
        return redirect(reverse(url))
    else:
        messages.error(
            request, 'An error has occured while trying to delete the object')
        context["error_msg"] = "Deletion of record is unsuccessful"
        return render(request, 'detailview.html', context)


def get_obj_data(model_name):
    data = []
    if model_name == "Human":
        data = HumanModel.objects.all()
    elif model_name == "Home":
        data = HomeModel.objects.all()
    elif model_name == "Breed":
        data = BreedModel.objects.all()
    elif model_name == "Cat":
        data = CatModel.objects.all()
    return data


def get_filter_data(data, start_date=None, end_date=None):

    if start_date and end_date:
        filter_data = data.filter(
            created__gte=start_date, created__lte=end_date)
    elif start_date:
        filter_data = data.filter(created__gte=start_date)
    elif end_date:
        filter_data = data.filter(created__lte=end_date)
    else:
        filter_data = data

    return filter_data


def export_csv(request):
    if request.method == "GET":
        return render(request, 'export_csv.html')

    elif request.method == "POST":
        data = get_obj_data(request.POST['selected-model'])
        start_date = request.POST.get('start')
        end_date = request.POST.get('end')

        filter_data = get_filter_data(data, start_date, end_date)

        df_data = pd.DataFrame([data.__dict__ for data in filter_data])
        df_data.drop('_state', axis=1, inplace=True)
        df_data.set_index('id', inplace=True)

        csv_buffer = io.StringIO()
        df_data.to_csv(csv_buffer)

        response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=model.csv'

        return response


class Human:

    class List(ListView):
        model = HumanModel
        template_name = 'listview.html'

    class Detail(DetailView):
        model = HumanModel
        template_name = 'detailview.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            cat_list = HumanModel.objects.get(id=self.kwargs.get('pk'))
            context['cat_count'] = cat_list.cat_set.count()
            context['cat_list'] = cat_list.cat_set.all()
            return context

    class Form(CreateView):
        form_class = HumanForm
        template_name = 'form.html'
        success_url = '/human'

    def edit_human(request, pk):
        human = get_object_or_404(HumanModel, id=pk)
        return edit(request, HumanForm, human, 'sitecat:human-detail', pk)

    def delete_human(request, pk):
        human = get_object_or_404(HumanModel, id=pk)
        return delete(request, human, 'human', 'sitecat:human-list', pk)


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

    def delete_cat(request, pk):
        cat = get_object_or_404(CatModel, id=pk)
        return delete(request, cat, 'cat', 'sitecat:cat-list', pk)


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

    def delete_home(request, pk):
        home = get_object_or_404(HomeModel, id=pk)
        return delete(request, home, 'home', 'sitecat:home-list', pk)


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

    def delete_breed(request, pk):
        breed = get_object_or_404(BreedModel, id=pk)
        return delete(request, breed, 'breed', 'sitecat:breed-list', pk)
