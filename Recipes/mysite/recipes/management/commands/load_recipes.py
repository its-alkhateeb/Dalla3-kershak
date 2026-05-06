import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Load recipes from JSON file into the database'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(
            settings.BASE_DIR,
            'recipes',
            'recipes.json'
        )

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        created_count = 0
        skipped_count = 0

        for item in data['recipes']:
            recipe, created = Recipe.objects.get_or_create(
                name=item['name'],
                defaults={
                    'category': item.get('category', ''),
                    'description': item.get('description', ''),
                    'calories': item.get('calories', ''),
                    'serves': item.get('serves', ''),
                    'prep_time': item.get('prep_time', ''),
                    'ingredients': "\n".join(item.get('ingredients', [])),
                    'instructions': "\n".join(item.get('instructions', [])),
                }
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created: {item["name"]}'))
            else:
                skipped_count += 1
                self.stdout.write(self.style.WARNING(f'  - Skipped (already exists): {item["name"]}'))

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {created_count} recipes created, {skipped_count} skipped.'
        ))