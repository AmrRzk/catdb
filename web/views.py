from django.views.generic import TemplateView, ListView

from .models import Human, Cat, Breed, Home


class IndexView(TemplateView):
    template_name = "index.html"


class HumanListView(ListView):
    model = Human
    template_name = 'humanlist.html'

    def get_queryset(self):
        return Human.objects.all()
