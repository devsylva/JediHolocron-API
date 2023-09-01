from django.db import models
from django.contrib.auth import get_user_model
import uuid


class Film(models.Model):
    title = models.CharField(max_length=255)
    comment_count = models.PositiveIntegerField(default=0)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete_and_update_comment_count(self):
        # Decrement the comment count of the associated film
        self.film.comment_count -= 1
        self.film.save()
        # Delete the comment
        self.delete()

    def __str__(self):
        return f"Comment on {self.film.title}"
