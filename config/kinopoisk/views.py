from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/main.html', {'movies': movies})

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/movies_list.html', {'movies': movies})

def actors_list(request):
    actors = MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR)
    return render(request, 'kinopoisk/actors_list.html', {
        'persons': actors, 'title': 'Актёры'
    })

def directors_list(request):
    directors = MoviePerson.objects.filter(role=MoviePerson.RoleType.DIRECTOR)
    return render(request, 'kinopoisk/directors_list.html', {
        'persons': directors, 'title': 'Режиссёры'
    })

def sound_endgineers_list(request):
    sound_endgineers = MoviePerson.objects.filter(role=MoviePerson.RoleType.SOUND_ENGINEER)
    return render(request, 'kinopoisk/sound_endgineers_list.html', {
        'persons': sound_endgineers, 'title': 'Звукорежиссёры'
    })
    

def genres_list(request):
    genres = Movie.objects.all()
    return render(request, 'kinopoisk/genres_list.html', {'genres': genres})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'kinopoisk/main.html', {'movie': movie})

def actor_detail(request, actor_id):
    actor = Movie.objects.get(id=actor_id)
    movies = actor.acted_in_movies.all()
    return render(request, 'kinopoisk/actor_detail.html', {
        'person': actor, 'movies':movies
    })

def director_detail(request, director_id):
    director = Movie.objects.get(id=director_id)
    movies = director.directed_movies.all()
    return render(request, 'kinopoisk/director_detail.html', {
        'person': director, 'movies':movies
    })

def sound_endgineer_detail(request, sound_endgineer_id):
    sound_endgineer = Movie.objects.get(id=sound_endgineer_id)
    movies = sound_endgineer.sounded_movies.all()
    return render(request, 'kinopoisk/sound_endgineer.html', {
        'person': sound_endgineer, 'movies':movies
    })

def genre_detail(request, genre_id):
    genre = Movie.objects.get(id=genre_id)
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': genre, 'moveis': movies
    })