from django.urls import path
from .views import (
    FilmView,
    FilmDetail,
    CommentView
)

urlpatterns = [
    path("films/", FilmView.as_view()),
    path("film/<int:pk>/", FilmDetail.as_view()),
    path("comments/", CommentView.as_view()),
]