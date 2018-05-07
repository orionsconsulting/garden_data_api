from rest_framework import serializers
from garden_data.submodel.garden_data import GardenData

class GardenDataSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    observation_timestamp = serializers.DateTimeField()
    weather_station = serializers.IntegerField()
    soil_temp = serializers.DecimalField(max_digits=4, decimal_places=1)
    air_temp = serializers.DecimalField(max_digits=4, decimal_places=1)
    soil_moisture = serializers.DecimalField(max_digits=4, decimal_places=1)

    def create(self, validated_data):
        return GardenData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.observation_timestamp = validated_data.get('observation_timestamp', instance.observation_timestamp)
        instance.weather_station = validated_data.get('weather_station', instance.weather_station)
        instance.soil_temp = validated_data.get('soil_temp', instance.soil_temp)
        instance.air_temp = validated_data.get('air_temp', instance.air_temp)
        instance.soil_moisture = validated_data.get('soil_moisture', instance.soil_moisture)
        instance.save()
        return instance