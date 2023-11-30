import datetime

from django.db.models import *


class Moisture(Model):
    fertilizer = FloatField()
    soil = FloatField()
    light = FloatField()
    air_temp = FloatField()
    day_id = ForeignKey('TimeLine', null=1, on_delete=CASCADE)
    date_id = ForeignKey('Day', null=1, on_delete=CASCADE)

    def __str__(self):
        return str({'день': self.date_id, 'время суток': self.day_id, 'fert': self.fertilizer})


class TimeLine(Model):
    """ Тип дня("День", "Вечер", "Утро" и "Ночь" ) """
    id = AutoField(primary_key=True)
    type = CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return str({'id': self.id, 'type': self.type})


class Day(Model):
    """ Таблица с датой """
    id = AutoField(primary_key=True)
    date = DateField(null=False)

    def __str__(self):
        return str({'id': self.id, 'date': self.date})
