from django.core.management.base import BaseCommand
from WeatherApp.views import *


class Command(BaseCommand):
    help = 'Store Weather data'

    def handle(self, *args, **kwargs):
        fetchFromS3AndStoreToDB()
        self.stdout.write("Data saved successfully.")