#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from WeatherApp.models import *
from django.http import HttpResponse
import requests
import datetime
from django.views.decorators.csrf import csrf_exempt

from WeatherApp.serializer import *

@csrf_exempt
def storeWeatherData(request):
    if request.method != 'POST':
        return HttpResponse('Request method should be POST.')

    try:
        fetchFromS3AndStoreToDB()
        return HttpResponse('Data Saved Successfully....')
    except:
        return HttpResponse('Server Error....')


def fetchFromS3AndStoreToDB():
    metricsList = Metrics.objects.all()
    if metricsList.count() == 0:
        setMetricsLocationData()

    metricsList = Metrics.objects.all()
    locationsList = Locations.objects.all()
    for metric in metricsList:
        for location in locationsList:
            url = \
                'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/' \
                + metric.mName + '-' + location.lName + '.json'
            weatherData = requests.get(url).json()
            dataTobeStored = list()
            for object in weatherData:
                dataTobeStored.append(Weather(wValue=object['value'],
                        wDate=datetime.date(year=object['year'],
                        month=object['month'], day=1), metricsId_id=1,
                        locationsId_id=1))
            Weather.objects.bulk_create(dataTobeStored)


def setMetricsLocationData():
    metricsdata = list()
    metricsdata.append(Metrics(mName='Tmax'))
    metricsdata.append(Metrics(mName='Tmin'))
    metricsdata.append(Metrics(mName='Rainfall'))
    Metrics.objects.bulk_create(metricsdata)
    locationsdata = list()
    locationsdata.append(Locations(lName='UK'))
    locationsdata.append(Locations(lName='England'))
    locationsdata.append(Locations(lName='Scotland'))
    locationsdata.append(Locations(lName='Wales'))
    Locations.objects.bulk_create(locationsdata)


def getWeatherData(request):
    startDate = datetime.datetime.strptime(request.GET.get('startDate'
            ), '%Y-%m-%d').date()
    endDate = datetime.datetime.strptime(request.GET.get('endDate'),
            '%Y-%m-%d').date()
    metricType = request.GET.get('metricType')
    location = request.GET.get('location')
    weatherDataList = getWeatherDataFromDB(startDate, endDate,
            metricType, location)
    serializerData = WeatherSerializer(weatherDataList, many=True).data
    return JSONResponse(serializerData)


def getWeatherDataFromDB(
    startDate,
    endDate,
    metricType,
    location,
    ):
    weatherDataList = Weather.objects.filter(wDate__gte=startDate,
            wDate__lte=endDate, metricsId__mName=metricType,
            locationsId__lName=location)

    return weatherDataList
