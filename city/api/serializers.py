from rest_framework import serializers
from city.models import Province, City


class CitySerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ['name', 'province']


class ProvinceSerializer(serializers.ModelSerializer):
    cities = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        many=True,
        slug_field='city',

    )

    class Meta:
        model = Province
        fields = ['name', 'cities']
