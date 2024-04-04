from django.shortcuts import render

# Create your views here.
def actor_detail(request):
    return render(request, "cinema/actor_detail.html")

def composer_detail(request):
    return render(request, "cinema/composer_detail.html")

def director_detail(request):
    return render(request, "cinema/director_detail.html")

def genre_detail(request):
    return render(request, "cinema/genre_detail.html")

def movie_detail(request):
    return render(request, "cinema/movie_detail.html")

def producer_detail(request):
    return render(request, "cinema/producer_detail.html")

def movie_list(request):
    return render(request, "cinema/movie_list.html")

def movie_persons_list(request):
    return render(request, "cinema/movie_persons_list.html")

def screenwriter_detail(request):
    return render(request, "cinema/screenwriter_detail.html")
