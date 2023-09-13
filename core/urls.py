from django.urls import path
from .views import (
    FilmView,
    FilmDetail,
    CommentView,
    CommentDetail
)


app_name = "core"

urlpatterns = [
    path("films/", FilmView.as_view(), name="film-list"),
    path("film/<int:pk>/", FilmDetail.as_view(), name="film-detail"),
    path("comments/", CommentView.as_view(), name="comment-list"),
    path("comment/<int:pk>/", CommentDetail.as_view(), name="comment-detail"),
]