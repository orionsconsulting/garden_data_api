from rest_framework import serializers
from garden_data.submodel.weather_station import WeatherStation

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
        fields = ('id', 'weather_station', 'description')