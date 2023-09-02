from django.core.management.base import BaseCommand
from django.core import serializers
import os
from datetime import datetime
from django.conf import settings  
from core.models import Film, Comment
from user_app.models import User

class Command(BaseCommand):
    help = 'Backup user, film, and comment data'

    def handle(self, *args, **options):
        backup_dir = settings.BACKUP_DIR  # Use the BACKUP_DIR variable from settings
        os.makedirs(backup_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        # Backup user data
        user_backup_filename = f'users_{timestamp}.json'
        with open(os.path.join(backup_dir, user_backup_filename), 'w') as user_backup_file:
            serializers.serialize('json', User.objects.all(), indent=2, stream=user_backup_file)

        # Backup film data
        film_backup_filename = f'films_{timestamp}.json'
        with open(os.path.join(backup_dir, film_backup_filename), 'w') as film_backup_file:
            serializers.serialize('json', Film.objects.all(), indent=2, stream=film_backup_file)

        # Backup comment data
        comment_backup_filename = f'comments_{timestamp}.json'
        with open(os.path.join(backup_dir, comment_backup_filename), 'w') as comment_backup_file:
            serializers.serialize('json', Comment.objects.all(), indent=2, stream=comment_backup_file)

        self.stdout.write(self.style.SUCCESS(f'Backup completed. Data saved in {backup_dir}'))
