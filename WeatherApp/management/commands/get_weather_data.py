from django.core.management.base import BaseCommand
from WeatherApp.views import *
from django.core import serializers

class Command(BaseCommand):
    help = 'Get Weather data'

    def add_arguments(self, parser):
        parser.add_argument('startDate', type=str, help='Indicates the start date')
        parser.add_argument('endDate', type=str, help='Indicates the end date')
        parser.add_argument('metricType', type=str, help='Indicates the metrics type')
        parser.add_argument('location', type=str, help='Indicates the location name')


    def handle(self, *args, **kwargs):
        startDate = kwargs['startDate']
        endDate = kwargs['endDate']
        metricType = kwargs['metricType']
        location = kwargs['location']

        data = getWeatherDataFromDB(startDate, endDate, metricType, location)

        self.stdout.write(serializers.serialize('json', data))

