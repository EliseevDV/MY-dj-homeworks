import csv
from django.utils.text import slugify

from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options['filename']
        with open(filename, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_slug = slugify(phone['name'])
            phone_id = phone['id']
            Phone.objects.update_or_create(
                id=phone_id,
                defaults={
                    'name': phone['name'],
                    'price': phone['price'],
                    'image': phone['image'],
                    'release_date': datetime.strptime(phone['release_date'], '%Y-%m-%d'),
                    'lte_exists': bool(phone['lte_exists']),
                    'slug': phone_slug,
                }
            )



