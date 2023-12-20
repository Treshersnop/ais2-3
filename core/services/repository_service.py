from datetime import datetime
from typing import Optional, Iterable, List
from django.db.models import QuerySet
from ..models import Moisture, Day, TimeLine


"""

    Данный модуль является промежуточным слоем приложения, который отделяет операции 
    для работы с моделями DAO от основной бизнес-логики приложения. Создание данного 
    слоя позволяет унифицировать функции работы с источником данных, и, например, если 
    в приложении нужно будет использовать другой framework для работы с БД, вы можете 
    создать новый модуль (repository_service_newframework.py) и реализовать в нем функции 
    с аналогичными названиями (get_weather_by_city_id, и т.д.). Новый модуль можно будет
    просто импортировать в модуль с основной бизнес-логикой, практически не меняя при этом
    остальной код.
    Также отделение функций работы с БД можно сделать через отдельный абстрактный класс и 
    использовать порождающий паттерн для переключения между необходимыми реализацииями.

"""


def get_mois_by_date_id(id: int) -> Optional[Moisture]:
    """ Выборка одной записи об измерениях по идентификатору (PrimaryKey) дня """
    moisture = Moisture.objects.filter(date_id=id).first()
    return moisture


def get_mois_by_date_name(day_name: str) -> QuerySet:
    """ Выборка всех записей о погоде за определенное время суток """
    moisture = Moisture.objects.select_related('date_id').filter(date_id__type=day_name).all()
    return moisture

'''
def create_mois(fert: float, soil: float, light: float, air_temp: float, day_id: int, date_id: int) -> None:
    """ Создание нового объекта Moisture и добавление записи об измерении """
    moisture = Moisture.objects.create(fertilizer=fert, soil=soil, light=light, air_temp=air_temp, day_id_id=day_id, date_id_id=date_id)
    moisture.save()


def update_mois(fert: float, id: int) -> None:
    """ Обновление значений удобрения для заданного дня """
    moisture = get_mois_by_date_id(id)
    moisture.fertilizer = fert
    moisture.save()


def delete_mois_by_date_id(id: int) -> None:
    """ Удаление записей об измерении за указанный день """
    get_mois_by_date_id(id).delete()


def add_mois_day(date_name: datetime.date) -> None:
    date = Day.objects.create(date=date_name)
    date.save()

def add_mois_time_line(time_line_day: str) -> None:
    time_line_type = TimeLine.objects.create(type=time_line_day)
    time_line_type.save()
'''

