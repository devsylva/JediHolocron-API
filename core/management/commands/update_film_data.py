from django.core.management.base import BaseCommand
from core.models import Film, Comment 
import requests


class Command(BaseCommand):
    help = 'Fetch and update film data from external API'

    def handle(self, *args, **options):
        response = requests.get('https://swapi.dev/api/films') 
        data = response.json()
        film_data = data["results"]
        for i in film_data:
            film, created = Film.objects.update_or_create(
                # get film id from the url endpoint
                id=int(i['url'][28:-1]),
                defaults={
                    'title': i['title'],
                    'release_date': i['release_date'],
                }
            )

            # Retrieve existing comments for this film
            existing_comments = Comment.objects.filter(film=film)

            # Associate comments with the updated film
            for comment in existing_comments:
                comment.film = film
                comment.save()

        self.stdout.write(self.style.SUCCESS('Film data fetched and updated successfully'))
