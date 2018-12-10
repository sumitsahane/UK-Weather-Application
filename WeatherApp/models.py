from django.db import models
from django.db.models.signals import post_migrate
# Create your models here.

class Metrics(models.Model):
    mId = models.AutoField(primary_key=True)
    mName = models.CharField(max_length=200)

    class Meta:
        db_table = 'metrics'


class Locations(models.Model):
    lId = models.AutoField(primary_key=True)
    lName = models.CharField(max_length=200)

    class Meta:
        db_table = 'locations'


class Weather(models.Model):
    wId = models.AutoField(primary_key=True)
    wValue = models.CharField(max_length=200)
    wDate = models.DateField()
    metricsId = models.ForeignKey(Metrics,on_delete=models.DO_NOTHING)
    locationsId = models.ForeignKey(Locations,on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'weather'


# def insert_initial_data(**kwargs):
#     metricsdata = list()
#     metricsdata.append(Metrics(mName="Tmax"))
#     metricsdata.append(Metrics(mName="Tmin"))
#     metricsdata.append(Metrics(mName="Rainfall"))
#     Metrics.objects.bulk_create(metricsdata)
#     locationsdata = list()
#     locationsdata.append(Locations(lName="UK"))
#     locationsdata.append(Locations(lName="England"))
#     locationsdata.append(Locations(lName="Scotland"))
#     Locations.objects.bulk_create(locationsdata)
#
#
# post_migrate.connect(insert_initial_data)