from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data_table', views.data_table, name='data_table'),
    path('charts', views.charts, name='charts'),
    path('api/chart/data', views.ChartData.as_view()),
]