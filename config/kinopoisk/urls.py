from django.urls import path
from kinopoisk.views import *

urlpatterns = [
    path('actor_detail/',actor_detail,name='actor_detail' ),
    path('composer_detail/',composer_detail,name='composer_detail' ),
    path('director_detail/',director_detail,name='director_detail' ),
    path('movie_detail/',movie_detail,name='movie_detail' ),
    path('movie_list/',movie_list,name='movie_list' ),
    path('movie_persons_list/',movie_persons_list,name='movie_persons_list' ),
    path('producer_detail/',producer_detail,name='producer_detail' ),
    path('screenwriter_detail/',screenwriter_detail,name='screenwriter_detail' ),
    path('genre_detail/',genre_detail,name='genre_detail' ),
  
]