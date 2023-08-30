from django.core.management.base import BaseCommand
from core.models import Film, Comment 
import requests

class Command(BaseCommand):
    help = 'Fetch and update film data from external API'

    def handle(self, *args, **options):
        response = requests.get('https://swapi.dev/api/films') 
        data = response.json()

        for film_data in data:
            film, created = Film.objects.update_or_create(
                # Use a unique identifier from the API data, like film ID
                id=film_data['id'],
                defaults={
                    'title': film_data['title'],
                    'description': film_data['description'],
                    'release_date': film_data['release_date'],
                    # Map other fields
                }
            )

            # Retrieve existing comments for this film
            existing_comments = Comment.objects.filter(film=film)

            # Associate comments with the updated film
            for comment in existing_comments:
                comment.film = film
                comment.save()

        self.stdout.write(self.style.SUCCESS('Film data fetched and updated successfully'))
