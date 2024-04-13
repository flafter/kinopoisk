from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('movies_list/', movies_list, name='movies_list'),
    path('actors_list/', actors_list, name='actors_list'),
    path('directors_list/',directors_list, name='directors_list'),
    path('sound_endgineers_list/', sound_endgineers_list, name='sound_endgineers_list'),
    path('genres_list/', genres_list, name='genres_list'),
    path(
        'movie_detail/<int:movie_id>/', 
         movie_detail, name='movie_detail'
    ),
    path(
        'actor_detail/<int:actor_id>/', 
         actor_detail, name='actor_detail'
    ),
    path(
        'director_detail/<int:director_id>/', 
         director_detail, name='director_detail'
    ),
    path(
        'sound_endgineer_detail/<int:sound_endgineer_id>/', 
         sound_endgineer_detail, name='sound_endgineer'
    ),
    path(
        'genre_detail/<int:genre_id>/', 
         genre_detail, name='genre_detail'
    ),
]
