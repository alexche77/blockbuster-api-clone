from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blockbuster_clone.movies import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)