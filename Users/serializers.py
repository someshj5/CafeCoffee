from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

# class UserRoleSerializer(models.ModelSerializer):

#     class Meta:
#         model = 'user_role'
#         fields = '__all__'

#     def create(self, validated_data):
#         return user_role.objects.create
