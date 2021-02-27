import os
from django.conf import settings
from django.core.management.base import BaseCommand
from garpix_qa.main import run_qa


class Command(BaseCommand):
    help = 'Checking the Django project for quality'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Verbose mode',
        )

    def handle(self, *args, **options):
        directory = os.path.abspath(os.path.join(settings.BASE_DIR))
        verbose = options['verbose']
        run_qa(directory, verbose)
