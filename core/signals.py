from django.db.models.signals import post_save
from .models import Comment, Film
from django.dispatch import receiver


"""
auto increment the film comment count field after each comment is saved
"""
@receiver(post_save, sender=Comment)
def update_film_comment_count(sender, instance, created, **kwargs):
    if created:
        try:
            film = Film.objects.get(id=instance.film.id)
            film.comment_count += 1
            film.save()
        except Exception as e:
            pass