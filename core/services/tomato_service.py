from ..serializers import MoistureSerializer, DateSerializer
from .repository_service import *


"""

    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class TomatoService:


    def get_mois_in_day(self, day_id: int) -> Optional[MoistureSerializer]:
        result = get_mois_by_date_id(day_id)
        if result is not None:
            return MoistureSerializer(result)
        return result

    def get_all_moin_in_timeline(self, time_name: str) -> MoistureSerializer:
        result = get_mois_by_time_day_name(time_name.lower())
        mois_data = MoistureSerializer(result, many=True)     # для возвращения списка объектов, необходимо создание сериализатора с аргументом many=True
        return mois_data


    def add_mois_info(self, mois: MoistureSerializer) -> None:
        mois_data = mois.data     # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        create_mois(fert=mois_data.get('fertilizer'),
                    soil=mois_data.get('soil'),
                    light=mois_data.get('light'),
                    air_temp=mois_data.get('air_temp'),
                    day_id=mois_data.get('day_id_id'),
                    date_id=mois_data.get('date_id_id')
                    )


    def update_mois_info(self, mois: MoistureSerializer) -> None:
        mois_data = mois.data
        return update_mois(fert=mois_data.get('fertilizer'),
                           id=mois_data.get('date_id_id')
                           )


    def delete_mois_info_by_date_id(self, date_id: int) -> None:
        delete_mois_by_date_id(date_id)


    def add_date(self, date: DateSerializer) -> None:
        date_data = date.data
        add_mois_day(date_name=date_data.get('date'))

