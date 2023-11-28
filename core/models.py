import datetime

from django.db import models


class Moisture(models.Model):
    fertilizer = models.FloatField()
    soil = models.FloatField()
    light = models.FloatField()
    air_temp = models.FloatField()
    day_id = models.ForeignKey('Timeline', null="NULL", on_delete=models.CASCADE)
    date_id = models.ForeignKey('Day', null=datetime.datetime, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fertilizer}, день = {self.date_id}, время суток = {self.day_id}'


class TimeLine(models.Model):
    """ Тип дня("День", "Вечер", "Утро" и "Ночь" ) """
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return str({'id': self.id, 'type': self.type})


class Day(models.Model):
    """ Таблица с датой """
    id = models.AutoField(primary_key=True)
    date = models.DateField()

    def __str__(self):
        return str({'id': self.id, 'date': self.date})
