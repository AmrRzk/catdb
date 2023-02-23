from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('human', views.Human.List.as_view(), name='human-list'),
    path('human/<int:pk>/', views.Human.Detail.as_view(), name='human-detail'),
    path('human/create/', views.Human.Create.as_view(), name='human-create'),

    path('cat', views.Cat.List.as_view(), name='cat-list'),
    path('cat/<int:pk>/', views.Cat.Detail.as_view(), name='cat-detail'),
    path('cat/create/', views.Cat.Create.as_view(), name='cat-create'),

    path('home', views.Home.List.as_view(), name='home-list'),
    path('home/<int:pk>/', views.Home.Detail.as_view(), name='home-detail'),
    path('home/create/', views.Home.Create.as_view(), name='home-create'),

    path('breed', views.Breed.List.as_view(), name='breed-list'),
    path('breed/<int:pk>/', views.Breed.Detail.as_view(), name='breed-detail'),
    path('breed/create/', views.Breed.Create.as_view(), name='breed-create'),

]
