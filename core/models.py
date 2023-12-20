import datetime

from django.db.models import *


class Moisture(Model):
    fertilizer = FloatField()
    soil = FloatField()
    light = FloatField()
    air_temp = FloatField()
    date = ForeignKey('Day', null=1, on_delete=CASCADE)
    time = ForeignKey('TimeLine', null=1, on_delete=CASCADE)

    def __str__(self):
        return str({'день': self.date, 'время суток': self.time, 'fert': self.fertilizer})


class TimeLine(Model):
    """ Тип дня("День", "Вечер", "Утро" и "Ночь" ) """
    id = AutoField(primary_key=True)
    value1 = IntegerField()
    value2 = IntegerField()

    def __str__(self):
        return str({'id': self.id, 'hour': self.value1, 'minute': self.value2})


class Day(Model):
    """ Таблица с датой """
    id = AutoField(primary_key=True)
    date = DateField(null=False)

    def __str__(self):
        return str({'id': self.id, 'date': self.date})
