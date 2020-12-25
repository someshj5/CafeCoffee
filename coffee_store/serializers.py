from rest_framework import serializers
from .models import *


class AmenitySerialiers(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        # fields = ['name', 'description']
        fields = '__all__'

    def create(self, validated_data):
        return Amenity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)


class CoffeeSerializer(serializers.ModelSerializer):

    # amenities = serializers.PrimaryKeyRelatedField(
    #     queryset=Amenity.objects.all(), many=True)
    # amenities = AmenitySerialiers(many=True)

    class Meta:
        model = coffee_store
        # fields = ['name', 'address', 'city', 'state', 'email']
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        print('under create method of COffeeSerializeres', validated_data)
        return coffee_store.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.email = validated_data.get('email', instance.email)
        instance.amenities = set(validated_data.get('amenities',
                                                    instance.amenities))
        instance.save()
        return instance


class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
