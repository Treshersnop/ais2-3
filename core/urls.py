from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="AuTomato API",
      default_version='v1',
      description="AuTomato API",
      terms_of_service="https://example.com",
      contact=openapi.Contact(email="contact@mail.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('info/', views.Info.as_view(), name='info'),
    path('tomatoforecast/', views.GetPostPutTomato.as_view()),
    path('tomatoforecast/<str:day_name>', views.GetDelAllTomato.as_view()),
    #path('day/', views.PostDay.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
