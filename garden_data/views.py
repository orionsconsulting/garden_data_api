from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from garden_data.submodel.weather_station import WeatherStation
from garden_data.serializers import WeatherStationSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data=data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def weather_station_list(request):
    if request.method == 'GET':
        weather_station = WeatherStation.objects.all()
        weather_station_serializer = WeatherStationSerializer(weather_station, many=True)
        return JSONResponse(weather_station_serializer.data)
    elif request.method == 'POST':
        weather_station_data = JSONParser().parse(request)
        weather_station_serializer = WeatherStationSerializer(data=weather_station_data)
        if weather_station_serializer.is_valid():
            weather_station_serializer.save()
            return JSONResponse(weather_station_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(weather_station_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def weather_station_detail(request,pk):
    try:
        weather_station = WeatherStation.objects.get(pk=pk)
    except WeatherStation.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        weather_station_serializer = WeatherStationSerializer(weather_station)
        return JSONResponse(weather_station_serializer.data)

    elif request.method == 'PUT':
        weather_station_data = JSONParser().parse(request)
        weather_station_serializer = WeatherStationSerializer(weather_station, data=weather_station_data)
        if weather_station_serializer.is_valid():
            weather_station_serializer.save()
            return JSONResponse(weather_station_serializer.data)
        else:
            return JSONResponse(weather_station_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        weather_station.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)