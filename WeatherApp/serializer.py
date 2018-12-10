from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from WeatherApp.models import *


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ('wDate', 'wValue')


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)