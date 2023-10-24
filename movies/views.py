from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie
from movies.models import MovieCredit, MovieReview

def index(request):
    movies = Movie.objects.all()  # Obtener todas las películas
    context = {'movies': movies}
    return render(request, "movies/index.html", context)



def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    genres = movie.genres.all()  # Obtener los géneros asociados a la película
    movie_credits = MovieCredit.objects.filter(movie=movie)
    movie_reviews = MovieReview.objects.filter(movie=movie)
    
    # Imprimir los géneros para depuración
    for genre in genres:
        print(f"Género: {genre.name}")
    


    context = {'movie': movie, 'genres': genres,'movie_credits': movie_credits,'movie_reviews': movie_reviews}
    return render(request, "movies/movie_detail.html", context=context)

def Ejemplo(request):
    movies = Movie.objects.all()
    context = {'movie_list': movies}
    return render(request, "movies/Ejemplo.html", context=context)

def Basic(request):
    movies = Movie.objects.all()
    context = {'movie_list': movies}
    return render(request, "movies/Basic.html", context=context)

# Create your views here.
