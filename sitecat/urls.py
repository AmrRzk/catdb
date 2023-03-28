from django.urls import path

from . import views

app_name = "sitecat"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('export', views.export_csv, name='export-csv'),


    path('human', views.Human.List.as_view(), name='human-list'),
    path('human/<int:pk>/', views.Human.Detail.as_view(), name='human-detail'),
    path('human/create/', views.Human.Form.as_view(), name='human-create'),
    path('human/edit/<int:pk>/', views.Human.edit_human, name='human-edit'),
    path('human/delete/<int:pk>/', views.Human.delete_human, name='human-delete'),

    path('cat', views.Cat.List.as_view(), name='cat-list'),
    path('cat/<int:pk>/', views.Cat.Detail.as_view(), name='cat-detail'),
    path('cat/create/', views.Cat.Form.as_view(), name='cat-create'),
    path('cat/edit/<int:pk>/', views.Cat.edit_cat, name='cat-edit'),
    path('cat/delete/<int:pk>/', views.Cat.delete_cat, name='cat-delete'),

    path('home', views.Home.List.as_view(), name='home-list'),
    path('home/<int:pk>/', views.Home.Detail.as_view(), name='home-detail'),
    path('home/create/', views.Home.Form.as_view(), name='home-create'),
    path('home/edit/<int:pk>/', views.Home.edit_home, name='home-edit'),
    path('home/delete/<int:pk>/', views.Home.delete_home, name='home-delete'),

    path('breed', views.Breed.List.as_view(), name='breed-list'),
    path('breed/<int:pk>/', views.Breed.Detail.as_view(), name='breed-detail'),
    path('breed/create/', views.Breed.Form.as_view(), name='breed-create'),
    path('breed/edit/<int:pk>/', views.Breed.edit_breed, name='breed-edit'),
    path('breed/delete/<int:pk>/', views.Breed.delete_breed, name='breed-delete'),

]
