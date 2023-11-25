from django.core.management.base import BaseCommand
from django.db import transaction

from profiles.factories import ProfileFactory, BioFactory

class Command(BaseCommand):
    help = 'Generate random profiles and bio data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of profiles to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        with transaction.atomic():
            for _ in range(total):
                profile = ProfileFactory()
                BioFactory(profile=profile)
            self.stdout.write(self.style.SUCCESS(f'Successfully created {total} profiles and bio data'))
