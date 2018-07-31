from django.conf.urls import url
from garden_data import views

urlpatterns = [
    url(r'^weather_station/$', views.weather_station_list),
    url(r'^weather_station/(?P<pk>[0-9]+)/$', views.weather_station_detail),
    url(r'^garden_data/$', views.garden_data_list),
    url(r'^garden_data/$', views.garden_data_detail)
]
