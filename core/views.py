from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status

from .serializers import MoistureSerializer, DateSerializer
from .services.tomato_service import TomatoService

service = TomatoService()


class Homepage(View):
    def get(self, request):
        context = {'text': 'Привет, Регина, Камилла, Бика, Катя и Лина!', 'title': 'Главная страница'}
        return render(request=request, template_name='core/mainpage.html', context=context)


class Info(View):
    def get(self, request):
        context = {'title': 'Информация'}
        return render(request=request, template_name='core/info.html', context=context)


class GetDelAllTomato(GenericAPIView):
    serializer_class = MoistureSerializer    # определяем сериализатор (необходимо для генерирования страницы Swagger)
    renderer_classes = [JSONRenderer]       # определяем тип входных данных

    def get(self, request: Request, day_name: str) -> Response:
        """ Получение всех записей об измерении за определенный промежуток времени (утро, день или др.)"""
        response = service.get_all_moin_in_day(day_name)
        return Response(data=response.data)
'''
    def delete(self, request: Request, date_id: int) -> Response:
        """ Удаление всех записей об измерениях за определенный день """
        service.delete_mois_info_by_date_id(date_id)
        return Response(status=status.HTTP_200_OK)
'''

class GetPostPutTomato(GenericAPIView):
    serializer_class = MoistureSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Выборка одной записи об измерениях по идентификатору дня (необходим параметр day_id_id) """
        date_id = request.query_params.get('date_id')        # получаем параметр id из адреса запроса, например: /api/weatherforecast?city_id=1
        if date_id is None:
            return Response('Expecting query parameter?date_id= ', status=status.HTTP_400_BAD_REQUEST)
        response = service.get_mois_in_day(int(date_id))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись об измерении """
        serializer = MoistureSerializer(data=request.data)
        if serializer.is_valid():
            service.add_mois_info(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, *args, **kwargs) -> Response:
        """ Обновить самую старую запись об измерении """
        serializer = MoistureSerializer(data=request.data)
        if serializer.is_valid():
            service.update_mois_info(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PostDay(CreateAPIView):
    serializer_class = DateSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новый день измерения """
        serializer = DateSerializer(data=request.data)
        if serializer.is_valid():
            service.add_date(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
'''