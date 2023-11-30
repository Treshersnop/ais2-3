from django.test import TestCase
from .services.repository_service import *

"""
   Данный модуль реализует "тестовые случаи/ситуации" для модуля repository_service.
   Для создания "тестового случая" необходимо создать отдельный класс, который наследует 
   базовый класс TestCase. Класс django.test.TestCase является подклассом unittest.TestCase 
   стандартного Python модуля для тестирования - unittest.

   Более детально см.: https://docs.djangoproject.com/en/4.1/topics/testing/overview/
"""


class TestWeatherRepositoryService(TestCase):
    """ Все тестовые методы в классе TestCase (по соглашению)
        должны начинаться с префикса test_* """

    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        # создаем тестовые записи
        add_mois_time_line('night')
        add_mois_day('2023-01-01')
        create_mois(fert=2.36, soil=1.02, light=11.2, air_temp=10.2, day_id=1, date_id=1)

    def test_get_weather(self):
        """ Тест функции поиска записи Weather по наименованию населённого пункта """
        mois_in_time_line = get_mois_by_time_day_name(time_line_name='night')
        for row in mois_in_time_line:
            print(row)
            self.assertIsNotNone(row)  # запись должна существовать
            self.assertTrue(row.day_id_id == 1)  # идентификатор city_id == 1 (т.е. город UFA в таблице city)
            self.assertTrue(row.day_id.type == 'night')  # проверка связи по FK

    def test_delete_mois(self):
        """ Тест функции удаления записи Weather по наименованию населённого пункта """
        delete_mois_by_date_id(id=1)
        result = get_mois_by_date_id(id=1)  # ищем запись по идентификатору города UFA
        self.assertIsNone(result)  # запись не должна существоват


    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        pass

