from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'role',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating', 'duration',)

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'movie', 'created_at',)
