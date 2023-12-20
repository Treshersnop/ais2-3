from rest_framework import serializers

"""
    В данном модуле реализуются сериализаторы DRF, позволяющие 
    валидировать данные для моделей DAO (models.py), 
    а также сериализующие (преобразующие) эти модели в стандартные 
    объекты Python (dict) и в формат json. Подробнее см.: 
    https://www.django-rest-framework.org/api-guide/serializers/
    https://www.django-rest-framework.org/api-guide/fields/

    Сериализаторы DRF являются аналогом DTO для Django. 
"""


class MoistureSerializer(serializers.Serializer):
    fertilizer = serializers.FloatField()
    soil = serializers.FloatField()
    light = serializers.FloatField()
    air_temp = serializers.FloatField()
    date_id = serializers.IntegerField()
    time_id = serializers.IntegerField()

    """ Класс Serializer позволяет переопределить наследуемые 
        методы create() и update(), в которых, например, можно реализовать бизнес-логику 
        для сохранения или обновления валидируемого объекта (например, для DAO ) """


class DateSerializer(serializers.Serializer):
    name = serializers.DateField()
