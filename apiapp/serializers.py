from rest_framework import serializers
from apiapp import models


class HelloSerializer(serializers.Serializer):
    """Serializers a field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'surname', 'password')
        extra_kwargs = {
        'password': {
            'write_only':True,
            'style': {'input_type':'password'}
         }
        }


    def create(self, validated_data):
       """we have to change the default user so that our password is in * Type and to add our userprofilemanager structures"""
       user = models.UserProfile.objects.create_user(
           email = validated_data['email'],
           name = validated_data['name'],
           surname = validated_data['surname'],
           password = validated_data['password']
       )
       return user
