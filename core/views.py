from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Film, Comment
from .serializers import FilmSerializer, CommentSerializer
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page


# Create your views here.
class WelcomeView(APIView):
    permission_classes = [AllowAny]

    def get(sef, requset, format=None):
        return Response({
            "project name": "JediHolocron API",
            "author": "Ejike Sylva",
            "stack": {
                "language": "Python",
                "framework": "Django",
                "database": "PostgreSQL"
            },
            "api doc": "https://jediholocron-3afedfa6d6ce.herokuapp.com/api/doc/",
            "github repo": "https://github.com/devsylva/JediHolocron-API",
        }, status=status.HTTP_200_OK)


class FilmView(APIView):
    permission_classes = [IsAuthenticated]
    """
    list all films in ascending order by release date
    """
    # @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def get(self, request, format=None):
        films = Film.objects.all().order_by("release_date")
        serializer = FilmSerializer(films, many=True)
        return Response({
            "count": films.count(),
            "results": serializer.data 
        }, status=status.HTTP_200_OK)


class FilmDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    retrieve a film instance
    """
    def get(self, request, pk, format=None):
        film = get_object_or_404(Film, pk=pk)
        serializer = FilmSerializer(film)
        return Response({
            "film": serializer.data,
            "comment count": Comment.objects.filter(film=film).count(),
            "comments" : film.comment_set.all()
        }, status=status.HTTP_200_OK)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    """
    list all comment or create a new comment
    """
    # @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def get(self, request, format=None):
        comments = Comment.objects.all().order_by("created_at")
        serializer = CommentSerializer(comments,  many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message": "Comment Created",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    retrieve a comment instance
    """
    def get(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message": "comment updated",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk, user=request.user)
        comment.delete()
        return Response({
            "message": "Comment deleted"
        }, status=status.HTTP_204_NO_CONTENT)