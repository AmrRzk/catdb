from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('human', views.HumanListView.as_view(), name='human')
]
