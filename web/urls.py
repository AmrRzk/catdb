from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('human', views.HumanListView.as_view(), name='human-list'),
    path('human/<int:pk>/', views.HumanDetailView.as_view(), name='human-detail'),

    path('cat', views.CatListView.as_view(), name='cat-list'),
    path('cat/<int:pk>/', views.CatDetailView.as_view(), name='cat-detail'),

    path('home', views.HomeListView.as_view(), name='home-list'),
    path('home/<int:pk>/', views.HomeDetailView.as_view(), name='home-detail'),

    path('breed', views.BreedListView.as_view(), name='breed-list'),
    path('breed/<int:pk>/', views.BreedDetailView.as_view(), name='breed-detail')

]
