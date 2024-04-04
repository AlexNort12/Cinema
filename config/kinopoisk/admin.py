from django.contrib import admin
from kinopoisk.models import *


@admin.register(MoviePerson)
class MoviePerson(admin.ModelAdmin):
    list_display = (
        'name', 
        'role',
        'photo',
        'birth_date',
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name', 
        'description',
       
    )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'poster',
       
    )

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'id',
        'created_at',
        'likes',
    )
