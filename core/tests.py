from django.test import TestCase
import random
from .services.repository_service import *

"""
   Данный модуль реализует "тестовые случаи/ситуации" для модуля repository_service.
   Для создания "тестового случая" необходимо создать отдельный класс, который наследует 
   базовый класс TestCase. Класс django.test.TestCase является подклассом unittest.TestCase 
   стандартного Python модуля для тестирования - unittest.

   Более детально см.: https://docs.djangoproject.com/en/4.1/topics/testing/overview/
"""


class TestRepositoryService(TestCase):
    """ Все тестовые методы в классе TestCase (по соглашению)
        должны начинаться с префикса test_* """

    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        # создаем тестовые записи
        create_mois(fert=1.02, soil=random.uniform(20.0, 29.9), light=random.uniform(20.0, 29.9), air_temp=random.uniform(20.0, 29.9),
                       day_id=1, date_id=1)

    def test_get_weather(self):
        """ Тест функции поиска записи измерения по дате """
        moinsure = get_mois_by_date_id(1)
        print(moinsure)
        self.assertIsNotNone(moinsure)  # запись должна существовать
        self.assertTrue(moinsure.day_id == 1)  # идентификатор day_id == 1 (т.е. запись 1 января)

    def test_delete_weather(self):
        """ Тест функции удаления записи измерения по дате """
        delete_mois_by_date_id(1)
        result = get_mois_by_date_id(id=1)  # ищем запись по идентификатору даты
        self.assertIsNone(result)  # запись не должна существовать

    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        pass

