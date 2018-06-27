from rest_framework import serializers
from garden_data.submodel.weather_station import WeatherStation
from garden_data.submodel.garden_data import GardenData

class WeatherStationSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    weather_station = serializers.IntegerField()
    description = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return WeatherStation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.weather_station  = validated_data.get('weather_station', instance.weather_station)
        instance.description = validated_data.get('description', instance.description)

    class Meta:
        model = WeatherStation
        fields = ('pk', 'weather_station', 'description')

class GardenDataSerializer(serializers.HyperlinkedModelSerializer):
    weather_station_description = serializers.SlugRelatedField(queryset=WeatherStation.objects.all(),
                                                               slug_field='description')

    class Meta:
        model = GardenData
        fields = (
            'url',
            'pk',
            'observation_timestamp',
            'weather_station_description',
            'soil_temp',
            'air_temp',
            'soil_moisture'
        )