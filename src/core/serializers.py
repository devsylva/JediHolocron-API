from rest_framework import serializers
from .models import Film, Comment


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

