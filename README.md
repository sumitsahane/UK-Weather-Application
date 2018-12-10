# UK-Weather-Application
Django application using Django Rest Framework to store and retrieve UK weather data.

## Dependencies
```
Python 3.7.0
Django 2.1.4
djangorestframework 3.9.0
requests 2.20.0
```

## Configuration

* To create database tables:
```
python manage.py migrate
```

* To start Django server:
```
python manage.py runserver
```


## REST API

* Fetch data from S3 and store it in database(Request Method: POST, No parameters)
```
http://{host}/storeWeatherData/
```

* Get weather data from database(Request Method: GET)
Four parameters:
1) startDate
2) endDate
3) metricType
4) location

```
http://{host}/getWeatherData/?startDate=1990-02-01&endDate=1992-02-01&metricType=Tmax&location=UK
```

## Management commands

* Fetch data from S3 and store it in database
```
python manage.py store_weather_data
```

* Get weather data from database
Four parameters:
1) startDate
2) endDate
3) metricType
4) location

```
python manage.py get_weather_data "1990-02-01" "1992-02-01" "Tmax" "UK"
```


