from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Film, Comment
from .serializers import FilmSerializer, CommentSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_ratelimit.decorators import ratelimit


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
                "database": "PostgreSQL",
                "Version Control": "Git",
                "Hosting/Deployment": "Heroku",
            },
            "api doc": "https://jediholocron-3afedfa6d6ce.herokuapp.com/api/doc/",
            "github repo": "https://github.com/devsylva/JediHolocron-API",
            "postman test collection": "https://universal-firefly-869928.postman.co/workspace/5cd9b38b-31ec-4ae8-a146-aa6fce06363d"
        }, status=status.HTTP_200_OK)


class FilmView(APIView):
    permission_classes = [IsAuthenticated]

    """
    retrieve a list of films in ascending order with respect to release data

    Returns:
    - 200 OK: List of films
    - 401 Unauthorized: Authentication required
    """
    @method_decorator(ratelimit(key='user', rate='60/h', block=True))
    @method_decorator(cache_page(60 * 5))  # Cache for 5 minutes
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
    retrieve a film by ID

    This endpoint allows you to retrieve detailed information about a specific film by 
    providing its unique identifier (ID) in the URL.

    URL paramters:
    - `id` (int): The unique identifier of the film to retrieve

    Returns: 
    - 200 OK: Film found and returned successfully
    - 404 Not Found: Film with the provided ID does not exist.
    - 401 Unauthorized: Authentication required.

    """
    @method_decorator(ratelimit(key='user', rate='60/h', block=True))
    def get(self, request, pk, format=None):
        film = get_object_or_404(Film, pk=pk)
        serializer = FilmSerializer(film)
        comments = film.comments.all().order_by("created_at")
        commentserializer = CommentSerializer(comments, many=True)
        return Response({
            "film": serializer.data,
            "comment count": film.comments.count(),
            "comments" : commentserializer.data
        }, status=status.HTTP_200_OK)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    
    @method_decorator(ratelimit(key='user', rate='60/h', block=True))
    @method_decorator(cache_page(60 * 5))  # Cache for 5 minutes
    def get(self, request, format=None):
        """
        retrieve a list of all the comments in ascending order with respect to date created

        Returns:
        - 200 OK: List of comments
        - 401 Unauthorized: Authentication required
        """
        comments = Comment.objects.all().order_by("created_at")
        serializer = CommentSerializer(comments,  many=True)
        return Response(serializer.data)    

    @swagger_auto_schema(
        request_body=CommentSerializer,
        responses={201: "Comment created successfully"}
    )
    @method_decorator(ratelimit(key='user', rate='60/h', block=True))
    def post(self, request, format=None):
        """
        Create a new comment with custom parameters.
        """
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
    
    @method_decorator(ratelimit(key='user', rate='60/h', block=True))
    def get(self, request, pk, format=None):
        """
        retrieve a comment instance
        """
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(ratelimit(key='user', rate='60/h', block=True))
    def put(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk, user=request.user)
        if comment.user == request.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({
                    "message": "comment updated",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "You can't edit a comment that isn't yours"}, status=status.HTTP_403_FORBIDDEN)

    @method_decorator(ratelimit(key='user', rate='60/h', block=True))
    def delete(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.user == request.user:
            comment.delete_and_update_comment_count()
            return Response({
                "message": "Comment deleted"
            }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You can't delete a comment that isn't yours"}, status=status.HTTP_403_FORBIDDEN)