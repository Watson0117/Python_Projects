
from django.urls import path
from RidleyVerse import views

urlpatterns = [
    path('', views.RidleyVersehome, name='RidleyVerse-home'),
    path('Add-Movies/', views.AddMovies, name='Add-Movies'),
    path('List-Movies/', views.ListMovies, name='List-Movies'),
    path('<id>', views.MovieDetails, name='Movie-Details'),
    path('<id>/update/', views.EditMovies, name='Update'),
    path('<id>/delete/', views.DeleteMovies, name='Delete'),
    path('Full-Story/', views.GetRidleySoup, name='Full-Story')
    ]
